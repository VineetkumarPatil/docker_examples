import os
import socket
import random
import mysql.connector  # pip install mysql-connector-python
import sqlalchemy as db


'''
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'vineet',
    'password': 'vineet',
    'database': 'student_db'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')
'''


def get_mysql_db_connector():
    mydb = mysql.connector.connect \
            (
            host="localhost",    # localhost / mysql_db
            port='3306',
            user="testing",
            password="testing",
            database="vote_db"
        )
    return mydb


def insert_data_into_db(voter_id, vote):
    mydb = get_mysql_db_connector()
    mycursor = mydb.cursor()
    sql = "INSERT INTO vote_details (voter_id, vote) VALUES (%s, %s)"
    val = (voter_id, vote)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    print("successfully inserted")
    return "successfully inserted"




def initiate_the_program():
    vote = 'manual'
    voter_id = hex(random.getrandbits(64))[2:-1]
    print("voter_id :- " + str(voter_id))
    print("vote :- " + str(vote))
    insert_data_into_db(voter_id, vote)

if __name__ == '__main__':
    try:
        print('starting....')
        initiate_the_program()
    except Exception as e:
        print('ERROR : ' + str(e))
