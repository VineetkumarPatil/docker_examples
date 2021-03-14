# PostgreSQL with Python App
---

##### Table of contents
* [Introduction](#introduction)
* [Requirements](#requirements)
* [Components/Tools](#components)
* [Prerequisites](#prerequisites)
* [Folder Structure](#projectstructure)
* [Installation](#installation)
* [Learning](#learning)
* [Bonus](#bonus) 
* [Support](#support)

##### Introduction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This is  a simple application demonstrating the usage of dockers and how can we fit multiple services in a single conatiner. The idea is to build a simple python application interacting with a postgresql database. We will club both python application and database in a single container showing off the ability of container to hold multiple services.

##### Requirements
 - A simple python applciation to interact to postgresql database.
 - PostgresSQL database with Postgis extension installed.

##### Components/Tools
- Python : for interatcion with database.
- PostgresSQL database : to store data.
- Docker : to host the containers.
- OS : Linux (Debian 10 64bit) to build docker and containers.

##### Prerequisites
- Linux OS 
- Docker is setup and running properly.

##### Folder Structure
<pre>
.
│   .dockerignore
│   Dockerfile
│   READ_ME.md
│
├───python_app
│       requirements.txt
│       test_postgres_connection.py
│
└───scripts
        postgis_tables.sql
        startup.sh
</pre>

##### Installation
* Step 1: Import the code from this git repo to the machine where docker is installed.
* Step 2: Edit the file - docker file (in case of any password / version change)
* Step 3: Run the following command in terminal to create and launch containers -
   - Note : 
``` bash
sudo docker build -t my_test_container_image .

sudo docker run -m 4GB --rm -P --name my_test_container_image my_test_container_image 
``` 
* Step 4: Check the status of containers  -
    - docker ps 
    - docker ps -a
    - docker images 

##### Learning
- Develop a flask application using python and deploy in docker.
- Setup a MySql database in docker.
- Bridge the applications to interact with eachother.

##### Bonus
- How can I login to conatiner or connect to DB ?
   * sudo docker exec -it my_test_container_image /bin/bash
   * psql -U postgres -d postgres -h localhost -c "SELECT * from products;"

- You can convert python app to python web(flask) app and keep the services up and running all the time. 


##### Support 
- Vineetkumar - vineetkumar.patil@gmail.com
- For any queries/suggestions, please feel free to drop an email.
