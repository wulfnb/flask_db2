# flask_db2
flask todo app running on ibm db2


# pull docker image of db if using docker
docker pull ibmcom/db2

# run db2 in docker

docker run -itd --name db2 --privileged=true -p 50000:50000 -e LICENSE=accept -e DB2INST1_PASSWORD=password -e DBNAME=testdb ibmcom/db2

This will connect to the "testdb" database using the user "db2inst1" and the password "password".


## Create table for todo

```
CREATE TABLE todo (
    id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    done BOOLEAN DEFAULT FALSE,
    added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
```

## install python3 (not tested this command)

> yum install gcc  xz python3 gcc-c++ gcc-gfortran freetype2-devel libpng-devel zeromq zeromq-devel lapack blas python3-devel

## Install pip packages 
> pip install -r requriements.txt


## Run application
> python app.py