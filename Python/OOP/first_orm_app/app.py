#! /home/melissa/my_environments/py3SQLAlchemyEnv/bin/python
from flask import Flask, render_template				# same as beforecopy
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first_orm_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key = True)
  first_name = db.Column(db.String(45))
  last_name = db.Column(db.String(45))
  email = db.Column(db.String(45))
  age = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, server_default=func.now())
  updated_at = db.Column(db.DateTime, server_default=func.now())

@app.route("/")
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)