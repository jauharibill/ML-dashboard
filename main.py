from flask import Flask, request, url_for, session, redirect, render_template
from markupsafe import escape
from random import randint
from flask_mysqldb import MySQL
from application.requests.onlineshop_request import OnlineshopRequest
from config.database import Database

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
configDB = Database(app)
myDB = MySQL(configDB.config)

@app.route("/", methods=['GET'])
def index():
    cur = myDB.connection.cursor()
    cur.execute("SELECT * FROM online_shop ORDER BY id DESC LIMIT 20")
    data = cur.fetchall()
    return render_template('index.html', onlineshop=data)

@app.route("/create", methods=['GET'])
def create():
    return render_template('create.html')

@app.route("/store", methods=['POST'])
def store():
    data = request.form
    value = OnlineshopRequest(data)
    cur = myDB.connection.cursor()
    cur.execute("INSERT INTO online_shop(id, administrative, administrative_duration, informational, informational_duration, productrelated, productrelated_duration, bouncerates, exitrates, pagevalues, specialday, month, operatingsystems, browser, region, traffictype, visitortype, weekend, revenue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (value.id, value.administrative, value.administrative_duration, value.informational, value.informational_duration, value.productrelated, value.productrelated_duration, value.bouncesrates, value.exitrates, value.pagevalues, value.specialday, value.month, value.operatingsystems, value.browser, value.region, value.traffictype, value.visitortype, value.weekend, value.revenue))
    myDB.connection.commit()
    return redirect(url_for('index'))

@app.route("/edit/<int:id>", methods=['GET'])
def edit(id):
    cur = myDB.connection.cursor()
    cur.execute("SELECT * FROM online_shop WHERE id=%s", (id,))
    data = cur.fetchone()
    return render_template('edit.html', onlineshop=data)

@app.route("/update/<int:id>", methods=['POST'])
def update(id):
    data = request.form
    value = OnlineshopRequest(data)
    cur = myDB.connection.cursor()
    cur.execute("UPDATE online_shop SET administrative=%s, administrative_duration=%s, informational=%s, informational_duration=%s, productrelated=%s, productrelated_duration=%s, bouncerates=%s, exitrates=%s, pagevalues=%s, specialday=%s, month=%s, operatingsystems=%s, browser=%s, region=%s, traffictype=%s, visitortype=%s, weekend=%s, revenue=%s WHERE id=%s", (value.administrative, value.administrative_duration, value.informational, value.informational_duration, value.productrelated, value.productrelated_duration, value.bouncesrates, value.exitrates, value.pagevalues, value.specialday, value.month, value.operatingsystems, value.browser, value.region, value.traffictype, value.visitortype, value.weekend, value.revenue, id))
    myDB.connection.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    cur = myDB.connection.cursor()
    cur.execute("DELETE FROM online_shop WHERE id=%s", (id,))
    myDB.connection.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()