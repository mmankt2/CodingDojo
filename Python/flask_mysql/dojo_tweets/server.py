#! /usr/bin/python3
from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt       
import re 
app = Flask(__name__)

app.secret_key = "super secret"
bcrypt = Bcrypt(app)
db='basic_registration'

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

@app.route('/dashboard')
def dashboard():
  mysql = connectToMySQL(db)
  query = "SELECT u1.first_name, u1.last_name, t.content, t.created_at, t.likes, t.id from tweets t join followers f on t.user_id = f.followed_id join users u on f.follower_id = u.id join users u1 on f.followed_id = u1.id where u.id = %(id)s order by t.id desc;"
  q_data = {
    'id':session['id']
  }
  results = mysql.query_db(query,q_data)
  print(results)  
  return render_template('dashboard.html',tweets=results)

@app.route('/tweet/create', methods=["POST"])
def tweet():
  mysql = connectToMySQL(db)
  if 'id' not in session:
    flash('You must login to create a tweet')
    return redirect('/')
  is_valid = True
  if len(request.form['tweet'])<1:
    flash('tweet must contain some content')
    is_valid = False
    return redirect('/dashboard')
  query = "INSERT INTO tweets (content,user_id,created_at,updated_at) values(%(content)s,%(id)s,NOW(),NOW());"
  q_data = {
    'content':request.form['tweet'],
    'id':session['id']
  }
  mysql.query_db(query,q_data)
  mysql = connectToMySQL(db)
  query = "SELECT u1.first_name, u1.last_name, t.content, t.created_at, t.likes, t.id from tweets t join followers f on t.user_id = f.followed_id join users u on f.follower_id = u.id join users u1 on f.followed_id = u1.id where u.id = %(id)s order by t.id desc;"
  q_data = {
    'id':session['id']
  }
  results = mysql.query_db(query,q_data)
  print(results)  
  return render_template('/dashboard.html', tweets = results)

@app.route('/add_like/<id>', methods=["POST","GET"])
def add_like(id):
  mysql = connectToMySQL(db)
  query = "UPDATE tweets set likes = likes + 1 where id = %(id)s;"
  q_data = {
    'id':id
  }
  mysql.query_db(query,q_data)
  mysql = connectToMySQL(db)
  query = "SELECT * from tweets where id = "+q_data['id']+";"
  results = mysql.query_db(query)
  print(results)
  return redirect('/dashboard')

@app.route('/tweets/<id>/delete', methods=["POST","GET"])
def delete_tweet(id):
  mysql = connectToMySQL(db)
  query = "DELETE from tweets where id = %(id)s;"
  q_data = {
    'id':id
  }
  mysql.query_db(query,q_data)
  mysql = connectToMySQL(db)
  query = "SELECT * from tweets where id = "+q_data['id']+";"
  results = mysql.query_db(query)
  print(results)
  return redirect('/dashboard')


@app.route('/tweets/<id>/edit')
def edit_tweet(id):
  mysql = connectToMySQL(db)
  query = "SELECT * from tweets where id = %(id)s;"
  q_data = {
    'id':id
  }
  results = mysql.query_db(query,q_data)
  print(results)
  return render_template('edit_tweet.html', tweet = results[0])

@app.route('/tweets/<id>/update', methods=["POST"])
def update_tweet(id):
  mysql = connectToMySQL(db)
  if 'id' not in session:
    flash('You must login to create a tweet')
    return redirect('/')
  is_valid = True
  if len(request.form['tweet'])<1:
    flash('tweet must contain some content')
    is_valid = False
    return redirect('/dashboard')
  query = "UPDATE tweets set content = %(new_content)s, updated_at = NOW() where id = %(id)s;"
  q_data = {
    'id':id,
    'new_content':request.form['tweet']
  }
  results = mysql.query_db(query,q_data)
  print(results)
  return redirect('/dashboard')

@app.route('/users')
def show_users():
  mysql = connectToMySQL(db)
  query = "SELECT u1.first_name, u1.last_name, u1.email, u1.id, f1.follower_id from users u1 left join followers f1 on f1.followed_id = u1.id and f1.follower_id = %(id)s where u1.id <> %(id)s;"
  q_data = {
    'id':session['id']
  }
  users = mysql.query_db(query,q_data)
  print(users)
  return render_template('/show_users.html', users = users)

@app.route('/follow/<uid>')
def follow(uid):
  mysql = connectToMySQL(db)
  query = "INSERT INTO followers (follower_id, followed_id, created_at, updated_at) values (%(id)s, %(uid)s, NOW(), NOW());"
  q_data = {
    'id':session['id'],
    'uid':uid
  }
  fid = mysql.query_db(query,q_data)
  print(fid)
  return redirect('/users')

@app.route('/unfollow/<uid>')
def unfollow(uid):
  mysql = connectToMySQL(db)
  query = "DELETE FROM followers where follower_id = %(id)s and followed_id = %(uid)s;"
  q_data = {
    'id':session['id'],
    'uid':uid
  }
  mysql.query_db(query,q_data)
  return redirect('/users')

if __name__ == "__main__":
  app.run(debug=True)