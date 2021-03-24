
from flask import Flask, redirect, render_template, flash, blueprints, jsonify
from flask import request, session
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
import psycopg2


app = Flask(__name__)

app.secret_key = '123'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://qigueenywepswf:6dfe096b778783f1d5932be9516b36a87c14cf8cb007a8dca4546f47060021c3@ec2-3-211-37-117.compute-1.amazonaws.com:5432/d5193g7acku5on'
db = SQLAlchemy(app)




def interact_db(query, query_type: str):
    return_value = False
    connection = psycopg2.connect(host='ec2-3-211-37-117.compute-1.amazonaws.com',
                                  user='qigueenywepswf',
                                  password='6dfe096b778783f1d5932be9516b36a87c14cf8cb007a8dca4546f47060021c3',
                                  dbname='d5193g7acku5on')

    cursor = connection.cursor()
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/request', methods=['GET', 'POST'])
def code():
    mobile = False
    if 'codeid' in request.args:
        current_id = request.args['codeid']
        session['id'] = True
        session['code'] = current_id
        query = "SELECT * FROM users WHERE id ='%s'" % current_id
        query_result = interact_db(query, query_type='fetch')

    agent = request.headers.get('User-Agent')
    if ('iphone' or 'android' or 'blackberry') in agent.lower():
        mobile = True
    if (mobile == True):
        return render_template('instructions.html', id=current_id, user=query_result)
    else:
        return render_template('video1.html')





@app.route('/instructions')
def instructions():
    return render_template('instructions.html')


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/PreTest')
def pretest():
    return render_template("PreTest.html")


@app.route('/video1')
def video1():
    return render_template("video1.html")


@app.route('/video2')
def video2():
    return render_template("video2.html")


@app.route('/afterTest')
def afterTest():
    return render_template("afterTest.html")


@app.route('/demog')
def demog():
    return render_template("demog.html")


@app.route('/requestend')
def requestend():
    return render_template("end.html")


@app.route('/requestPre')
def requestpre():
    return render_template("video1.html")


@app.route('/end')
def end():
    return render_template("end.html")


@app.route('/timer')
def timer():
    return render_template("Timer.html")


if __name__ == '__main__':
    app.run()
