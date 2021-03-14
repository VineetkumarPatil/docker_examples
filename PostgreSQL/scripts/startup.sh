#!/bin/bash
echo "Welcome to start up script"
echo "Executing the statements"
echo '------------------------------------------------------------------------------------------------'
echo "running the POSTGIS SQL DB (in background)..."
echo "stopping the service (if exists/locked)..."
echo `service postgresql stop`
echo "Removing the locked PID file(if exists)..."
echo `rm /var/run/postgresql/.s.PGSQL.5432.lock`
echo "stopping the service (if exists/locked)..."
echo `service postgresql stop`
nohup sh -c "/usr/lib/postgresql/9.6/bin/postgres -D /var/lib/postgresql/9.6/main -c config_file=/etc/postgresql/9.6/main/postgresql.conf &"
echo "POSTGIS SQL Up and Running"
sleep 30 # sleep for 30seconds.
/python_app/venv/bin/python3.7 /python_app/test_postgres_connection.py
echo "All programs running finsihed...."
echo '------------------------------------------------------------------------------------------------'
