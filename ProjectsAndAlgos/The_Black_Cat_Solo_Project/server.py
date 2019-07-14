#!/usr/bin/env python
from __future__ import print_function
from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt       

#below lines needed for google calendar API integration
import datetime
import pickle
import os.path
import re 

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
calendaridPT = '9n16t54iligakcd64916che4gs@group.calendar.google.com'

#needed for flask
app = Flask(__name__)
app.secret_key = "super secret"
bcrypt = Bcrypt(app)
db='the_black_cat'

#users:id, first name, last name, email, password, created at, updated at
#sessions: id, day, time, session length, user_id, notes
#blogs: id, content, user_id, created at, updated at
#comments: id, content, user_id, blog_id, created_at, updated_at

#allow more special characters in the regex
pw_regex = re.compile(r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w\d]{8,}$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
  return render_template('homepage.html')

@app.route('/login-register')
def registration_page():
  return render_template('registration.html')

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
  if is_valid == True:
    query = "SELECT * from users where email = lower(%(email)s);"
    q_data = {
      'email':email
    }
    user_info = mysql.query_db(query,q_data)
    if user_info:
      flash('Email already registered. Please login.')
      return redirect('/login-register')
    pw_hash = bcrypt.generate_password_hash(pw)
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
  return redirect('/login-register')

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
        session['user_email'] = email
        session['first_name'] = user_info[0]['first_name']
        session['id'] = user_info[0]['id']
        return redirect('/')
      else:
        flash('Password or email is incorrect.')
        return redirect('/login-register')
  return redirect('/')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


@app.route('/myaccount/<id>')
def edit(id):
  mysql = connectToMySQL(db)
  query = "SELECT * from users where id = %(id)s;"
  q_data = { 'id':id}
  data = mysql.query_db(query,q_data)
  return render_template('myaccount.html',id=id,data=data[0])

@app.route('/users/<id>/update', methods=["POST"])
def update_user(id):
  mysql = connectToMySQL(db)
  query = "UPDATE users set first_name=%(fn)s, last_name=%(ln)s, email=%(email)s, updated_at=NOW() where id=%(id)s;"
  print(id)
  q_data = {
    'id':id,
    'fn':request.form['first_name'],
    'ln':request.form['last_name'],
    'email':request.form['email']
  }
  mysql.query_db(query,q_data)
  flash('Successfully updated user')
  return redirect('/myaccount/'+str(id))

@app.route('/users/<id>/destroy')
def delete(id):
  mysql = connectToMySQL(db)
  query = "DELETE from users where id=%(id)s;"
  q_data = {'id':id}
  mysql.query_db(query,q_data)
  flash('User deleted')
  session.clear()
  return redirect('/')

@app.route('/blog')
def blog():
  return render_template('blog-simple.html')

@app.route('/personaltraining/schedulesession')
def schedulesession():
  if 'id' not in session:
    return redirect('/personaltraining/schedulesession/login-register')
  return render_template('schedulesession.html')

@app.route('/personaltraining/schedulesession/login-register')
def schedulesessregistration():
  return render_template('schedulesesslogin.html')

@app.route('/register-schedulesession',methods=["POST"])
def registerpt():
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
  if is_valid == True:
    query = "SELECT * from users where email = lower(%(email)s);"
    q_data = {
      'email':email
    }
    user_info = mysql.query_db(query,q_data)
    if user_info:
      flash('Email already registered. Please login.')
      return redirect('/personaltraining/schedulesession/login-register')
    pw_hash = bcrypt.generate_password_hash(pw)
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
  return redirect('/personaltraining/schedulesession')

@app.route('/login-schedulesession',methods=["POST"])
def loginpt():
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
      return redirect('/personaltraining/schedulesession/login-register')
    else:#check if password matches
      print(user_info[0])
      if bcrypt.check_password_hash(user_info[0]['password'],request.form['password']) == True:
        print('password matched')
        session['user_email'] = email
        session['first_name'] = user_info[0]['first_name']
        session['id'] = user_info[0]['id']
        return redirect('/personaltraining/schedulesession')
      else:
        flash('Password or email is incorrect.')
        return redirect('/personaltraining/schedulesession/login-register')
  return redirect('/personaltraining/schedulesession')

@app.route('/createevent')
def createevent():
  #get form data
  creds = None
  # The file token.pickle stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)

  service = build('calendar', 'v3', credentials=creds)

  # Call the Calendar API
  now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

  event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
      'dateTime': '2019-07-28T09:00:00-07:00',
      'timeZone': 'America/Los_Angeles',
  },
  'end': {
      'dateTime': '2019-07-28T17:00:00-07:00',
      'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
      'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
      {'email': 'lpage@example.com'},
      {'email': 'sbrin@example.com'},
  ],
  'reminders': {
      'useDefault': False,
      'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
      ],
  },
  }

  event = service.events().insert(calendarId=calendaridPT, body=event).execute()
  return redirect('/personaltraining/calendar')


if __name__ == "__main__":
  app.run(debug=True)