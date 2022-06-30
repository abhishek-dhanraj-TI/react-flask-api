import time
import mysql.connector
import requests
import os

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

API2_TIME_URL = os.environ.get("API2_TIME_URL", None)
print("API2 Time URL => ", API2_TIME_URL)

@app.route('/')
def hello_world():
  return 'Hello, Docker!'

@app.route('/api-1-time')
def get_current_time():
    r = requests.get(url = API2_TIME_URL)
    print("Response => ", r)
    data = r.json()
    print("Response.json : data => ", data)
    return {'time': data['time']} 
    
@app.route('/val')
def get_val():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p@ssw0rd1",
    database="db"
    )
    cursor = mydb.cursor()
    print('hello')
    cursor.execute("SELECT * FROM count")
    count = cursor.fetchall()
    cursor.close()
    print('hello2')
    print(count)
    return dict(count)



@app.route('/initdb')
def initdb():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p@ssw0rd1"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS db")
    cursor.execute("CREATE DATABASE db")
    cursor.close()

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p@ssw0rd1",
    database="db"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS count")
    cursor.execute("CREATE TABLE count (counter int)")
    cursor.close()
    return "db Initialized"

if __name__ == "__main__":
  app.run(host ='0.0.0.0')
