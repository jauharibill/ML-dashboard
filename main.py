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
    cur.close()
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
    cur.close()
    return redirect(url_for('index'))