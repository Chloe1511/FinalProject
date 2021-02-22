from datetime import timedelta

from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = '123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/instructions')
def instructions():
    return render_template("instructions.html")


if __name__ == '__main__':
    app.run()
