from flask import Flask

app = Flask(__name__)
# app.config.from_object('config')
from app import redis_app
from app import mysql_app

from flask import render_template, flash, redirect, session, url_for, request, g, Markup


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/getredis')
def getredis():
	msg=redis_app.main()
	return msg



@app.route('/getmysql')
def getmysql():
	msg=mysql_app.SqlOperator.main()
	return "Who dares to answer the MYSQL query :\n\n" + str(msg)
