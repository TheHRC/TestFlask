from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Persons(db.Model):
    __tablename__ = 'persons'
    personid = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)