# Voting App
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
* [Developers](#developers)

##### Introduction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This is  a simple application demonstrating the usage of dockers. The idea is to build a simple web application for voting process. The app should be ease of use and must be plug and play type.

##### Requirements
 - A web application for users to cast their vote. 
 - Store the voting results in a database.
 - A web application to show the aggregated results of the votings.

##### Components/Tools
- Flask-Python : to develop web application.
- MySql database : to store voting results.
- Html-Css : styling and front end appearances. 
- Docker : to host the applications.
- OS : Linux (Debian 10 64bit)

##### Prerequisites
- Linux OS 
- Docker is setup and running properly.


##### Folder Structure
<pre>
.
├── Docker_App_steps.txt
├── docker_compose_detailed.yml
└── vote_app
    ├── Dockerfile
    ├── driver.py
    ├── requirements.txt
    ├── static
    │   └── stylesheets
    │       └── style.css
    ├── templates
    │   └── index.html
    └── test.py
</pre>

##### Installation
* Step 1: Import the code from this git repo to the machine where docker is installed.
* Step 2: Edit the file - docker_compose_detailed.yml
    - Step 2.1: In mysql_db section, under volumes, create your own folders and replace them.
    - Step 2.2 [optional step] : In mysql_db section, under environment, you can set your own passwords. If you change any password then make sure the new password is updated in  vote_app/driver.py file.
    - Step 2.3: Either change ther ports or else make sure the default ports 20001 and 3306 are open and not being used by any other application.
    - Step 3.4: Save the changes.
    - Step 3.5: To be on a safer side, cross check the values in vote_app/driver.py file. They should be same values as in docker_compose_detailed.yml file.
* Step 3: Run the following command in terminal to create and launch containers -
   - Note : -d runs the docker command in deattach mode.
``` bash
docker-compose -f /home/vineet/project_directory/docker-examples/VotingApp/docker_compose_detailed.yml up -d
``` 
* Step 4: Check the status of containers  -
    - docker ps 
    - docker ps -a
    - docker images 

* Step 5: Login into Mysql container and run below commands (this is one time setup) -
   - open terminal
   - docker exec -it mysql_db bash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :- now you are logged into mysql db container
   - mysql -u -p &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :- now your are logged into mysql database
   - Create database if not exists :- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; create database vote_db;
   - Create user if not exists :- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; create user 'testing'@'localhost' identified by 'testing';
   - Grant privileges :- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; grant all privileges on vote_db.* to 'testing'@'%' with grant option;
   - Create table :- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  CREATE TABLE `vote_details` (
  `voter_id` varchar(255),
  `vote` varchar(255) NOT NULL
) DEFAULT CHARSET=utf8
;
- Step 6: Your docker containers are setup now. 
   - URL to display/test : http://xx.xx.xx.xxx:20001/helloworld
   - URL to vote : http://xx.xx.xx.xxx:20001/





##### Learning
- Develop a flask application using python and deploy in docker.
- Setup a MySql database in docker.
- Bridge the applications to interact with eachother.

##### Bonus
- How can I retain my data if my container is destroyed ?
   * Tag/mount the voloume of the MySql database to one of the OS locations. 
   * Sample code (docker-compose.yml)- 
       mysql_db: 
        image: mysql
        container_name: mysql_db
        ###### volumes:
          - "/home/vineet/docker_practice/mysql_db_storage/:/var/lib/mysql"

- How can I copy the existing data to new DB ?
    * Use the above approach, once container is built it will have the exported/mounted data. 


##### Developers 
- Vineetkumar - vineetkumar.patil@gmail.com
- For any queries/suggestions, please feel free to drop an email.
