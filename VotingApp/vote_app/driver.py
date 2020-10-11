from flask import Flask, render_template, request, make_response, g
import os
import socket
import random
import json
import mysql.connector

app = Flask(__name__)

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()


def get_mysql_db_connector():
    mydb = mysql.connector.connect\
    (
        host="mysql_db",
        port= '3306',
        user="root",
        password="passwd",
        database="vote_db"
    )
    return mydb

def insert_data_into_db(voter_id,vote):
    mydb = get_mysql_db_connector()
    mycursor = mydb.cursor()
    sql = "INSERT INTO vote_details (voter_id, vote) VALUES (%s, %s)"
    val = (voter_id, vote)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    print("successfully inserted")
    return "successfully inserted"


@app.route("/", methods=['POST','GET'])
def hello():
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    print("volder id : " + str(voter_id))
    vote = None

    if request.method == 'POST':
        vote = request.form['vote']
        print("voter_id :- "+ str(voter_id))
        print("vote :- "+ str(vote))
        insert_data_into_db(voter_id, vote)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        hostname=hostname,
        vote=vote,
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp


@app.route("/helloworld", methods=['POST','GET'])
def helloworld():
    print("helloworld")
    return "Hello World...!!!"

'''
if __name__ == '__main__':
    print("starting the python program..........")
    ip = '0.0.0.0'
    #ip = 'localhost'
    app.run(host=ip, debug=True, threaded=True) # these can be added in config.yaml as well.
    #app.run(host='localhost', port=5000, debug=True, threaded=True)  # these can be added in config.yaml as well. Local testing
'''