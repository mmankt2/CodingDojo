#! /home/melissa/my_environments/py3SQLAlchemyEnv/bin/python
from flask import render_template,request,redirect			# same as beforecopy
from config import app, db, bcrypt, migrate
from models import Dojos, Ninjas 

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