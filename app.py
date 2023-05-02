from flask import Flask, render_template, request, redirect, url_for
import ibm_db

app = Flask(__name__)
conn = ibm_db.connect("DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=password;", "", "")

@app.route("/")
def index():
    tasks = []
    stmt = ibm_db.exec_immediate(conn, "SELECT * FROM todo")
    result = ibm_db.fetch_assoc(stmt)
    while result != False:
        tasks.append(result)
        result = ibm_db.fetch_assoc(stmt)
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    description = request.form["description"]
    ibm_db.exec_immediate(conn, f"INSERT INTO todo (title, description) VALUES ('{title}', '{description}')")
    return redirect("/")


@app.route('/update/<int:id>', methods=["POST"])
def update(id):
    print("UPDATE Call ", id)
    stmt = f"UPDATE todo SET done = 1 WHERE id = {id}"
    ibm_db.exec_immediate(conn, stmt)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    print("DELETE Call ", id)
    stmt = f"DELETE FROM todo WHERE id = {id}"
    ibm_db.exec_immediate(conn, stmt)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
