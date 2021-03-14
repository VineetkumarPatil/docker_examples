

# --------------------------------------------------------------------------------------------------------------------------------------------
# USING UBUNTU 16.04 AS BASE OS 
# --------------------------------------------------------------------------------------------------------------------------------------------

FROM ubuntu:16.04
RUN echo "Starting the build..."
RUN echo $pwd

# basic installation
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y curl
RUN apt-get install -y software-properties-common


# --------------------------------------------------------------------------------------------------------------------------------------------
# INSTALL PYTHON 3.7
# --------------------------------------------------------------------------------------------------------------------------------------------

RUN apt-get update 
RUN apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y curl python3.7 python3.7-dev python3.7-distutils

# Upgrade pip to latest version
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py &&\
    python3.7 get-pip.py --force-reinstall &&\
    rm get-pip.py
	
# Install python3 virtual env	
RUN apt-get install -y python3.7-venv 

RUN echo `python3 --version`

# --------------------------------------------------------------------------------------------------------------------------------------------
# INSTALL GDAL SERVICES  
# --------------------------------------------------------------------------------------------------------------------------------------------

RUN add-apt-repository -y ppa:ubuntugis/ppa
RUN apt update 
RUN apt upgrade # if you already have gdal 1.11 installed 
RUN apt install -y gdal-bin python-gdal python3-gdal # if you don't have gdal 1.11 already installed 

  

# --------------------------------------------------------------------------------------------------------------------------------------------
# INSTALL PYTHON APP 
# --------------------------------------------------------------------------------------------------------------------------------------------

RUN echo "Installing PYTHON APP "

RUN mkdir -p /python_app

RUN echo "----------- Installing Vitual Environment for :- python_app -----------"				  
				  
COPY ./python_app/requirements.txt /python_app/requirements.txt

# installing python app requirements - 	
RUN /bin/bash -c "cd /python_app &&\
				  ls -l &&\
				  python3.7 -m venv venv &&\
				  chmod 777 -R * &&\
				  source venv/bin/activate &&\
				  python3.7 -m pip install wheel &&\
				  python3.7 -m pip install -r /python_app/requirements.txt &&\
				  echo --------successfully_installed_requirements--------"	

			  
COPY ./python_app /python_app


# --------------------------------------------------------------------------------------------------------------------------------------------
# INSTALL POSTGIS SQL DATABASE
# --------------------------------------------------------------------------------------------------------------------------------------------

COPY ./scripts/postgis_tables.sql /postgis_tables.sql

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update 

# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc

RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" 
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt update
RUN apt-get install -y postgresql-9.6 postgresql-contrib-9.6
RUN echo `psql --version`
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable
RUN apt update
RUN apt install -y postgis postgresql-9.6-postgis-2.3



# Add postgres to sudo users ->
RUN apt-get update && apt-get -y install sudo
RUN echo "postgres:postgres" | chpasswd && adduser postgres sudo
 
USER postgres


# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `docker` owned by the ``docker`` role.
# Note: here we use ``&&\`` to run commands one after the other - the ``\``
#       allows the RUN command to span multiple lines.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    psql --command "ALTER USER postgres PASSWORD 'postgres';" &&\
    createdb -O docker docker &&\
	psql -a -f postgis_tables.sql

	
# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
#RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.6/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
#RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.3/main/postgresql.conf
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.6/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

RUN echo "***************POSTGIS INSTALLATION WAS SUCCESSFUL***************"

	
# --------------------------------------------------------------------------------------------------------------------------------------------
# TRIGGER DOCKER FILE 
# --------------------------------------------------------------------------------------------------------------------------------------------

COPY ./scripts/startup.sh /startup.sh

ENTRYPOINT ["/startup.sh"]

CMD ["bash","/startup.sh"] 

