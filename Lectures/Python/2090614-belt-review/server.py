#!/usr/bin/python3
#reference google doc https://docs/google.com/document/d/1SXf0-YkeQEUmyrobjtDloJGaGZpD5-W9uxaj5ccRM90/edit?usp=sharing

from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
app = Flask(__name__)
app.secret_key = "secret key"        
bcrypt = Bcrypt(app)

db = "enhanced_wall"

@app.route('/')
def index():
  #create a form on this html
  return render_template("index.html")

#create a route that the form from index will go to
#update database
@app.route('/register', methods=["POST"])
def register_user():
  is_valid = True
  if len(request.form['first_name']) < 2:
    is_valid = False
    flash("first name must be at least 2 chars long")
  if len(request.form['last_name']) < 2:
    is_valid = False
    flash("last name must be at least 2 chars long")
  (request.form['email'])
  if len(request.form['password']) < 8:
    is_valid = False
    flash("password must be at least 8 chars long")
  if request.form['cpassword'] != request.form['password']:
    is_valid = False
    flash("passwords do not match")
  if not EMAIL_REGEX.match(request.form['email']):
    is_valid = False
    flash("please use a valid email address")
  if is_valid:
    #create db connection
    #create query
    #pass valid data to query
    #send info to db
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    mysql = MySQLConnection(db)
    query = "INSERT INTO users(first_name, last_name,email,password,created_at,updated_at) values (%(fn)s,%(ln)s,%(email)s,%(pw)s,NOW(),NOW());"
    data = {
      'fn' : request.form['first_name'],
      'ln' : request.form['last_name'],
      'email' : request.form['email'],
      'pw' : pw_hash
    }
    user_id = mysql.query_db(query,data)
    session['user_id'] = user_id
    return redirect("/wall")
  
  return redirect('/')

@app.route('/login',methods=["POST"])
def login_user():
  is_valid = True
  if len(request.form['email'])<1:
    flash("please enter your email")
    is_valid = False
  if len(request.form['password'])<1:
    flash("please enter your password")
    is_valid = False
  if not is_valid:
    return redirect('/')
  else:
    #make sure email exists in db, then unhash password and check the passwords match
    mysql = MySQLConnection(db)
    query = "SELECT * from users where email = %(email)s;"
    data = {
      'email':request.form['email'].lower()
    }
    user = mysql.query_db(query,data)
    if user:
      hashed_password = user[0]['password']
      if bcrypt.check_password_hash(hashed_password, request.form['password']):
        session['user_id'] = user[0]['id']
        return redirect('/wall')
      else:
        flash("password is invalid")
        return redirect('/')
    else:
      flash("please use a valid email address")
  return redirect('/')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

@app.route("/wall")
def wall_landing():
  #make sure user is logged in
  if 'user_id' not in session:
    return redirect("/")
  query = "SELECT * from users where users.id = %(id)s;"
  data = {
    'id': session['user_id']
  }
  mysql = MySQLConnection(db)
  user = mysql.query_db(query,data)

  return render_template('wall.html', user=user[0])

if __name__ == "__main__":
  app.run(debug=True)