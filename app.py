#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_username = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')
cloud_sql_connection_name = os.getenv('CLOUD_SQL_CONNECTION_NAME')
database_uri = 'mysql+pymysql://' + db_name + ':' + db_pass + '@/' + db_name + '?unix_socket=/cloudsql/' + cloud_sql_connection_name
print(database_uri)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<db-user>:<db-password>@localhost:3306/<db-name>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'success!'})

@app.route('/test/post/<name>', methods=['GET'])
def upload(name):
    
    user = Test(name=name)
    db.session.add(user)
    db.session.commit()

    return jsonify({'status' : 'Saved in DB!'})

@app.route('/test/get/all', methods=['GET'])
def query():
    result = Test.query.all()
    mydict = {}
    for row in result:
        mydict[row.id] = row.name
    return jsonify(mydict)

if __name__ == '__main__':
    app.run()