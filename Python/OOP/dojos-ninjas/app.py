#! /home/melissa/my_environments/py3SQLAlchemyEnv/bin/python
from flask import Flask, render_template,request,redirect			# same as beforecopy
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func
from flask_migrate import Migrate			# this is new
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojos_ninjas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

@app.route('/')
def landing():
  all_dojos = Dojos.query.all()
  #print(all_dojos)
  #one_dojo = Dojos.query.get(1)
  #print(one_dojo)
  #print(dir(one_dojo))
  #print(one_dojo.ninjas)
  return render_template('index.html', all_dojos=all_dojos)

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
  #print(request.form)
  instance_of_dojo = Dojos(
    name=request.form['dojo_name'], 
    city=request.form['dojo_city'], 
    state = request.form['dojo_state']
    )
  print(type(instance_of_dojo))
  #print(instance_of_dojo)
  db.session.add(instance_of_dojo)
  db.session.commit()
  #all_dojos = Dojos.query.all()
  #print(all_dojos)
  return redirect('/')

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
  #print(request.form)
  instance_of_ninja = Ninjas(
    first_name=request.form['first_name'], 
    last_name=request.form['last_name'], 
    dojo_id = request.form['dojo']
    )
  #print(type(instance_of_ninja))
  #print(instance_of_ninja)
  db.session.add(instance_of_ninja)
  db.session.commit()
  return redirect('/')


if __name__ == "__main__":
  app.run(debug = True)