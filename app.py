from datetime import timedelta

from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = '123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/instructions')
def instructions():
    return render_template("instructions.html")


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


@app.route('/end')
def end():
    return render_template("end.html")


@app.route('/timer')
def timer():
    return render_template("Timer.html")


@app.route('/stam')
def stam():
    return render_template("stam.html")


if __name__ == '__main__':
    app.run()
