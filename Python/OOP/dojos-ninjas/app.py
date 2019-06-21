from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flas_migrate import Migrate
from sqlalchemy.sql import func
app = Flask()

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
  ninjas = db.relationship("Ninja",backref="dojos", lazy=True)
  created_at = db.Column(db.DatTime, server_default=func.now())
  updated_at = db.Column(db.DatTime, server_default=func.now(), onupdate=func.now())
  
class Ninjas(db.Model):
  __tablename__ = "ninjas"
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(45))
  last_name = db.Column(db.String(45))
  dojo_id = db.Column(db.Integer, db.ForeighKey('user_id'), nullable = False)
  # the below line could be used instead of the relationship in Dojos
  # dojos = db.relationship('Dojo', foreign_keys=[dojo_id], backref="dojo_ninjas",cascade="all")
  created_at = db.Column(db.DatTime, server_default=func.now())
  updated_at = db.Column(db.DatTime, server_default=func.now(), onupdate=func.now())

@app.route('/')
def landing():
  all_dojos = Dojo.query.all()
  one_dojo = Dojo.query.get(1)
  print(one_dojo)
  print(dir(one_dojo))
  print(one_dojo.dojo_ninjas)
  return render_template('index.html',all_dojos=all_dojos)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
  print(request.form)
  instance_of_dojo = Dojo(name=request.form['dojo_name]'], 
                          city=request.form['dojo_city'], 
                          state = request.form['dojo_state'])
  print(type(instance_of_dojo))
  print(instance_of_dojo)
  db.session.add(instance_of_dojo)
  db.session.commit()
  return redirect("/")

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
  print(request.form)
  instance_of_ninja = Dojo(first_name=request.form['first_name]'], 
                          last_name=request.form['last_name'], 
                          dojo_id = request.form['dojo'])
  print(type(instance_of_ninja))
  print(instance_of_ninja)
  db.session.add(instance_of_ninja)
  db.session.commit()
  return redirect("/")


if __name__ == "__main__":
  app.run(debug = True)