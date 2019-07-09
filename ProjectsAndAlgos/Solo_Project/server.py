#! /usr/bin/python3
from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt       
import re 
app = Flask(__name__)

app.secret_key = "super secret"
bcrypt = Bcrypt(app)
db='fit_ideas'

#users table: primary key, first, last, email, password, created at, updated at - DONE
#exercise table: primary key, exercise name, exercise description, exercise picture or gif, created at, updated at - DONE
#routine table: primary key, short description, date of last use, playlist link on spotify, created at, updated at - DONE
#exercises-routines table: primary key, exercise key, routine key - DONE
#exercise category 1 (standing, floor, abs)
#exercise cat 1-exercises: primary key, exercise key, exercise cat 1 key - DONE
#movement categories (push, pull, hinge, trunk rotation, single leg), - DONE
#movement categories-exercises: primary key, exercise key, exercise cat 2 key - DONE
#muscle group (hamstring, glutes, quads, calves, back, anterior delt, posterior delt, medial delt, pecs/chest, biceps, triceps)
#muscle group-exercises: primary key, exercise key, muscle group key

#allow more special characters in the regex
pw_regex = re.compile(r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,}$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
  #mysql = connectToMySQL(db)
  #query = "SELECT * from users;"
  #results = mysql.query_db(query)
  #print(results)
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
  email = request.form['email'].lower()

  if len(fn)<1:
    flash('First Name must be filled in.')
    is_valid = False
  if len(ln)<1:
    flash('Last Name must be filled in.')
    is_valid = False
  if not pw_regex.match(pw):
    flash('Password must be at least 8 characters in length, contain 1 upper case, 1 lower case, and 1 special character.')
    is_valid = False
  if not email_regex.match(email):
    flash('Please enter a valid email address.')
    is_valid = False
  if pw != cpw:
    flash('Passwords do not match.')
    is_valid = False
  if is_valid == True:
    query = "SELECT * from users where email = lower(%(email)s);"
    q_data = {
      'email':email
    }
    user_info = mysql.query_db(query,q_data)
    #print(user_info)
    if user_info:
      flash('Email already registered. Please login.')
      return redirect('/')
    pw_hash = bcrypt.generate_password_hash(pw)
    #print(pw_hash)
    flash('Successfully added new user!')
    
    mysql=connectToMySQL(db)
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) values (%(fn)s,%(ln)s,%(email)s,%(pw)s,NOW(),NOW());"
    q_data = {
      'fn':fn,
      'ln':ln,
      'email':email,
      'pw':pw_hash
    }
    id = mysql.query_db(query,q_data)
    #make a new user automaically follow themself
    mysql=connectToMySQL(db)
    query = "INSERT INTO followers (follower_id, followed_id, created_at, updated_at) values (%(id)s,%(id)s,NOW(),NOW());"
    q_data = {
      'id':id
    }
    fid = mysql.query_db(query,q_data)
  
  return redirect('/')

@app.route('/login',methods=["POST"])
def login():
  mysql = connectToMySQL(db)
  is_valid=True
  #get form info
  email = request.form['email'].lower()

  if len(request.form['password'])<1:
    flash('Password cannot be blank.')
    is_valid = False
  if len(email)<1:
    flash('Email cannot be blank.')
    is_valid = False
  if is_valid == True:
    query = "SELECT * from users where email = lower(%(email)s);"
    q_data = {
      'email':email
    }
    user_info = mysql.query_db(query,q_data)
    #print(user_info)
    if not user_info:
      flash('Email does not match a registered user')
      return redirect('/')
    else:#check if password matches
      print(user_info[0])
      if bcrypt.check_password_hash(user_info[0]['password'],request.form['password']) == True:
        print('password matched')
        #flash('Password or email is incorrect.')
        #return redirect('/')
      #else:
        session['user_email'] = email
        session['first_name'] = user_info[0]['first_name']
        session['id'] = user_info[0]['id']
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def success():
  if 'user_email' in session:
    return render_template('success.html')
  else:
    return redirect('/')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)