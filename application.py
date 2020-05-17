from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nszejgne:IuDxy3PBoxGQuPCVctpJ168uA9edUHyW@isilo.db.elephantsql.com:5432/nszejgne"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route('/')
def index():
    name = 'Hashib'
    return render_template('index.html',name=name)


@app.route('/get_persons/')
def get_persons():
    temp_view = 'list'
    persons = Persons.query.all()
    return render_template('persons.html',persons=persons,temp_view=temp_view)

@app.route('/get_persons/<int:personid>')
def person_details(personid):
    temp_view = 'detail'
    person = Persons.query.get(personid)
    return render_template('persons.html',person=person,temp_view=temp_view)

if __name__ == "__main__":
    app.run(debug=True)