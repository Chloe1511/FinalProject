from datetime import timedelta

from flask import Flask, redirect, render_template, flash, blueprints, jsonify
from flask import request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key= 'ldfjsolasfuasdfjsodfusoij4w09r8pswojufsldkfjdf9'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://qigueenywepswf:6dfe096b778783f1d5932be9516b36a87c14cf8cb007a8dca4546f47060021c3@ec2-3-211-37-117.compute-1.amazonaws.com:5432/d5193g7acku5on'
db = SQLAlchemy(app)

class users(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    PC_Mobile = db.Column(db.Boolean)
    Continuous_experiment = db.Column(db.Boolean)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/request', methods=['GET', 'POST'])
def code():

    if 'codeid' in request.args:
        current_id = request.args['codeid']
        session['id'] = True
        session['code'] = current_id
        #user = users.query.filter_by(ID=current_id).first()
        user = users(ID=124, PC_Mobile=True,Continuous_experiment=True)
        db.session.add(user)
        db.session.commit()
    return render_template('instructions.html', id=current_id)


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
