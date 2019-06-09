#! /usr/bin/python3
from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
app = Flask(__name__)

app.secret_key = "super secret"
bcrypt = Bcrypt(app)
database = 'login_register'

@app.route('/')
def signin():
  return render_template('signin.html')

@app.route('/register', methods=['POST'])
def register():
  pw_hash = bcrypt.generate_password_hash(request.form['password']) 
  is_valid = True
  if len(request.form['email'])<1:
    is_valid = False
    flash['email cannot be empty']
  if len(request.form['password'])<1:
    is_valid = False
    flash['must fill in a password']
  if request.form['password'] != request.form['confirm_password']:
    is_valid = False
    flash['passwords do not match']
  if not is_valid:
    return redirect('/')
  else:
    mysql = connectToMySQL(database)
    query = "INSERT INTO users (email, password, created_at, updated_at) values (%(email)s,%(password)s,NOW(),NOW());"
    data = {
      'email': request.form['email'],
      'password':pw_hash
    }
    user_id = mysql.query_db(query,data)
    session['user_id'] = user_id
    session['email'] = data['email']
  return redirect('/success')

@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
  mysql = connectToMySQL(database)
  query = "SELECT * from users where email = %(email)s;"
  data = {
    'email':request.form['email']
  }
  results = mysql.query_db(query,data)
  if len(results)>0:
    if bcrypt.check_password_hash(results[0]['password'],request.form['password']):
      session['user_id'] = use
      session['email'] = email
      return redirect('/success')
    else:
      flash("email and password do not match")
  else:
    flash("email not found")
  return redirect('/')


if __name__ == "__main__":
  app.run(debug=True)