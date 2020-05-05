#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql_alchemy_app:WHHzPPKdrURpNlsUZ4cBPJSKDp4o1WQ3@localhost:3306/sql_alchemy'
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