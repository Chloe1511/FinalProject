from flask import Flask, redirect, render_template, flash, blueprints, jsonify
from flask import request, session
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
import psycopg2
from sqlalchemy.sql.functions import now

app = Flask(__name__)
app.secret_key = '123'


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
    query_result=''
    if 'codeid' in request.args:
        current_id = request.args['codeid']
        session['id'] = True
        session['code'] = current_id
        query = "SELECT * FROM users WHERE id ='%s'" % current_id
        query_result = interact_db(query, query_type='fetch')

    current_id2 = session['code']
    query2 = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 1, current_timestamp )" % (current_id2)
    interact_db(query2, query_type='commit')
    if query_result == []:
        return render_template('instructions.html', id=current_id, user='')
    else:
        return render_template('instructions.html', id=current_id, user=query_result[0][1])


@app.route('/instructions')
def instructions():
    return render_template('instructions.html')


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/PreTest')
def pretest():
    return render_template("PreTest.html")


@app.route('/requestCheck')
def requestCheck():
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 3, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')
    check = ''
    if 'check' in request.args:
        check = request.args['check']
    if check == 'yes':
        current_id = session['code']
        query = "SELECT continuous_experiment FROM users WHERE id ='%s'" % current_id
        query_result = interact_db(query, query_type='fetch')
        return render_template("video1.html", ce=query_result[0])
    else:
        return render_template("home.html")


@app.route('/video1')
def video1():
    current_id = session['code']
    query = "SELECT continuous_experiment FROM users WHERE id ='%s'" % current_id
    query_result = interact_db(query, query_type='fetch')
   ## for qr in query_result:
     #   ce = qr.continuous_experiment

    return render_template("video1.html", ce=query_result[0])


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
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 8, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')

    if 'age' in request.args:
        ans2 = request.args['age']
    if 'gender' in request.args:
        ans3 = request.args['gender']
    if 'hoursPC' in request.args:
        ans4 = request.args['hoursPC']
    if 'hoursMob' in request.args:
        ans5 = request.args['hoursMob']
    if 'level' in request.args:
        ans6 = request.args['level']
    if 'open' in request.args:
        ans7 = request.args['open']
    if 'privace' in request.args:
        ans8 = request.args['privace']
    if 'big' in request.args:
        ans9 = request.args['big']
    if 'noisy' in request.args:
        ans10 = request.args['noisy']
    if 'dark' in request.args:
        ans11 = request.args['dark']
    if 'dense' in request.args:
        ans12 = request.args['dense']

    query2 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 1, '%s')" % (current_id, ans2)
    query3 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 2, '%s')" % (current_id, ans3)
    query4 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 3, '%s')" % (current_id, ans4)
    query5 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 4, '%s')" % (current_id, ans5)
    query6 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 5, '%s')" % (current_id, ans6)
    query7 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 6, '%s')" % (current_id, ans7)
    query8 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 7, '%s')" % (current_id, ans8)
    query9 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 8, '%s')" % (current_id, ans9)
    query10 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 9, '%s')" % (current_id, ans10)
    query11 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 10, '%s')" % (current_id, ans11)
    query12 = "INSERT INTO demog_quiz (id, qnumber, ans) VALUES ('%s', 11, '%s')" % (current_id, ans12)

    interact_db(query2, query_type='commit')
    interact_db(query3, query_type='commit')
    interact_db(query4, query_type='commit')
    interact_db(query5, query_type='commit')
    interact_db(query6, query_type='commit')
    interact_db(query7, query_type='commit')
    interact_db(query8, query_type='commit')
    interact_db(query9, query_type='commit')
    interact_db(query10, query_type='commit')
    interact_db(query11, query_type='commit')
    interact_db(query12, query_type='commit')

    return render_template("end.html")


@app.route('/requestPre')
def requestpre():
    current_id = session['code']
    query = "SELECT continuous_experiment FROM users WHERE id ='%s'" % current_id
    query_result = interact_db(query, query_type='fetch')

    if 'Q1' in request.args:
        ans1 = request.args['Q1']
    if 'Q2' in request.args:
        ans2 = request.args['Q2']
    if 'Q3' in request.args:
        ans3 = request.args['Q3']
    if 'Q4' in request.args:
        ans4 = request.args['Q4']
    if 'Q5' in request.args:
        ans5 = request.args['Q5']

    query1 = "INSERT INTO pre_test_quiz (id, qnumber, ans) VALUES ('%s', 1, '%s')" % (current_id, ans1)
    query2 = "INSERT INTO pre_test_quiz (id, qnumber, ans) VALUES ('%s', 2, '%s')" % (current_id, ans2)
    query3 = "INSERT INTO pre_test_quiz (id, qnumber, ans) VALUES ('%s', 3, '%s')" % (current_id, ans3)
    query4 = "INSERT INTO pre_test_quiz (id, qnumber, ans) VALUES ('%s', 4, '%s')" % (current_id, ans4)
    query5 = "INSERT INTO pre_test_quiz (id, qnumber, ans) VALUES ('%s', 5, '%s')" % (current_id, ans5)

    interact_db(query1, query_type='commit')
    interact_db(query2, query_type='commit')
    interact_db(query3, query_type='commit')
    interact_db(query4, query_type='commit')
    interact_db(query5, query_type='commit')

    return render_template("video1.html", ce=query_result[0])


@app.route('/requestAfter')
def requestafter():
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 7, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')

    if 'Q1' in request.args:
        ans1 = request.args['Q1']
    if 'Q2' in request.args:
        ans2 = request.args['Q2']
    if 'Q3' in request.args:
        ans3 = request.args['Q3']
    if 'Q4' in request.args:
        ans4 = request.args['Q4']
    if 'Q5' in request.args:
        ans5 = request.args['Q5']
    if 'Q6' in request.args:
        ans6 = request.args['Q6']
    if 'Q7' in request.args:
        ans7 = request.args['Q7']
    if 'Q8' in request.args:
        ans8 = request.args['Q8']
    if 'Q9' in request.args:
        ans9 = request.args['Q9']
    if 'Q10' in request.args:
        ans10 = request.args['Q10']


    query1 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 1, '%s')" % (current_id, ans1)
    query2 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 2, '%s')" % (current_id, ans2)
    query3 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 3, '%s')" % (current_id, ans3)
    query4 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 4, '%s')" % (current_id, ans4)
    query5 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 5, '%s')" % (current_id, ans5)
    query6 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 6, '%s')" % (current_id, ans6)
    query7 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 7, '%s')" % (current_id, ans7)
    query8 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 8, '%s')" % (current_id, ans8)
    query9 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 9, '%s')" % (current_id, ans9)
    query10 = "INSERT INTO knowledge_quiz (id, qnumber, ans) VALUES ('%s', 10, '%s')" % (current_id, ans10)

    interact_db(query1, query_type='commit')
    interact_db(query2, query_type='commit')
    interact_db(query3, query_type='commit')
    interact_db(query4, query_type='commit')
    interact_db(query5, query_type='commit')
    interact_db(query6, query_type='commit')
    interact_db(query7, query_type='commit')
    interact_db(query8, query_type='commit')
    interact_db(query9, query_type='commit')
    interact_db(query10, query_type='commit')

    return render_template("demog.html")



@app.route('/end')
def end():
    return render_template("end.html")


@app.route('/timer')
def timer():
    return render_template("Timer.html")



@app.route('/timestampIns')
def timestampIns():
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 2, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')
    return render_template("consent.html")

@app.route('/timestampVideo12')
def timestampVideo12():
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 4, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')
    return render_template("video2.html")

@app.route('/timestampVideo1Timer')
def timestampVideo1Timer():
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 4, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')
    return render_template("Timer.html")

@app.route('/timestampTimer')
def timestampTimer():
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 5, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')
    return render_template("video2.html")

@app.route('/timestampVideo2')
def timestampVideo2():
    current_id = session['code']
    query = "INSERT INTO timestamp_button (id, bnumber, times) VALUES ('%s', 6, current_timestamp )" % (current_id)
    interact_db(query, query_type='commit')
    return render_template("afterTest.html")

if __name__ == '__main__':
    app.run()
