from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
app = Flask(__name__)
app.secret_key = "keep it secret keep it safe"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojos_ninjas.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app) 
migrate = Migrate(app, db)


class Dojos(db.Model):
  __tablename__ = "dojos"
  #create the table here
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(45))
  city = db.Column(db.String(45))
  state = db.Column(db.String(45))
  ninjas = db.relationship("Ninjas",backref="dojos", lazy=True)
  created_at = db.Column(db.DateTime, server_default=func.now())
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
  
class Ninjas(db.Model):
  __tablename__ = "ninjas"
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(45))
  last_name = db.Column(db.String(45))
  dojo_id = db.Column(db.Integer, db.ForeignKey('dojos.id'), nullable = False)
  # the below line could be used instead of the relationship in Dojos
  # dojos = db.relationship('Dojo', foreign_keys=[dojo_id], backref="dojo_ninjas",cascade="all")
  created_at = db.Column(db.DateTime, server_default=func.now())
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
