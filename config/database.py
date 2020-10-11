from flask_mysqldb import MySQL

class Database:
    def __init__(self, app):
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'root'
        app.config['MYSQL_DB'] = 'ML'
        self.config = app
