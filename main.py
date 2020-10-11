from flask import Flask, request, url_for, session, redirect, render_template
from markupsafe import escape
from random import randint
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ML'
mysql = MySQL(app)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/create", methods=['GET'])
def create():
    return render_template('create.html')

@app.route("/store", methods=['POST'])
def store():
    details = request.form
    id = randint(10000, 20000)
    administrative = details['administrative']
    administrative_duration = details['administrative_duration']
    informational = details['informational']
    informational_duration = details['informational_duration']
    productrelated = details['productrelated']
    productrelated_duration = details['productrelated_duration']
    bouncesrates = details['bouncerates']
    exitrates = details['exitrates']
    pagevalues = details['pagevalues']
    specialday = details['specialday']
    month = details['month']
    operatingsystems = details['operatingsystems']
    browser = details['browser']
    region = details['region']
    traffictype = details['traffictype']
    visitortype = details['visitortype']
    weekend = details['weekend']
    revenue = details['revenue']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO online_shop(id, administrative, administrative_duration, informational, informational_duration, productrelated, productrelated_duration, bouncerates, exitrates, pagevalues, specialday, month, operatingsystems, browser, region, traffictype, visitortype, weekend, revenue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, administrative, administrative_duration, informational, informational_duration, productrelated, productrelated_duration, bouncesrates, exitrates, pagevalues, specialday, month, operatingsystems, browser, region, traffictype, visitortype, weekend, revenue))
    mysql.connection.commit()
    cur.close()
    return 'you store the data'

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        if request.form['username'] == "bill":
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return 'wrong username'
    else:
        return '''
            <form action="/login" method="POST">
                <input type="text" name="username">
                <button>login</button>
            </form>
        '''

