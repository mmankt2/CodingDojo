#! /usr/bin/python3
from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt       
import re 
app = Flask(__name__)

app.secret_key = "super secret"
bcrypt = Bcrypt(app)
db='basic_registration'

@app.route('/')
def index():
  mysql = connectToMySQL(db)
  query = "SELECT * from users;"
  results = mysql.query_db(query)
  print(results)
  return render_template('index.html')

@app.route('/register',methods=["POST"])
def register():
  mysql = connectToMySQL(db)
  is_valid=True
  #get form info
  fn = request.form['first_name']
  ln = request.form['last_name']
  pw = request.form['password']
  cpw = request.form['confirm_password']
  
  m = re.compile(r'[A-Za-z0-9@#$%^&+=]')
  if len(fn)<1:
    flash('First Name must be filled in.')
    is_valid = False
  if len(ln)<1:
    flash('Last Name must be filled in.')
    is_valid = False
  if not m.match(pw):
    flash('Password must be at least 8 characters in length, contain 1 upper case, 1 lower case, and 1 special character.')
    is_valid = False
  if len(pw)<8:
    flash('Password must be at least 8 characters in length, contain 1 upper case, 1 lower case, and 1 special character.')
    is_valid = False
  if pw != cpw:
    flash('Passwords do not match.')
    is_valid = False
  if is_valid == True:
    pw_hash =     bcrypt.generate_password_hash(pw)
    print(pw_hash)
    flash('Successfully added new user!')
    query = "INSERT INTO users (first_name, last_name, password, created_at, updated_at) values (%(fn)s,%(ln)s,%(pw)s,NOW(),NOW());"
    q_data = {
      'fn':fn,
      'ln':ln,
      'pw':pw_hash
    }
    id = mysql.query_db(query,q_data)
  return redirect('/')


if __name__ == "__main__":
  app.run(debug=True)