#! /home/melissa/my_environments/py3SQLAlchemyEnv/bin/python
from flask import render_template,request,redirect,flash,session		# same as beforecopy
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from config import app, db, bcrypt
import re 

#to create a many to many relationship between tweets and users
likes_table = db.Table('likes',
              db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
              db.Column('tweet_id', db.Integer, db.ForeignKey('tweets.id'),primary_key=True))

#to create a many to many relationship between user-followers and user-followeds
followers_table = db.Table('followers',
              db.Column('followed_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
              db.Column('follower_id', db.Integer, db.ForeignKey('users.id'), primary_key=True))

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key = True)
  first_name = db.Column(db.String(45))
  last_name = db.Column(db.String(45))
  email = db.Column(db.String(45))
  password = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, server_default=func.now())
  updated_at = db.Column(db.DateTime, server_default=func.now())
  tweets_this_user_likes = db.relationship('Tweet',secondary=likes_table)
  users_this_user_follows = db.relationship('User',
                            secondary=followers_table,
                            primaryjoin="User.id==followers.c.followed_id",
                            secondaryjoin="User.id==followers.c.follower_id")
  users_who_follow_this_user = db.relationship('User',
                            secondary=followers_table,
                            primaryjoin="User.id==followers.c.follower_id",
                            secondaryjoin="User.id==followers.c.followed_id")

class Tweet(db.Model):
  __tablename__ = "tweets"
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.Text)
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', foreign_keys=[author_id], backref="user_tweets")#, cascade="all")
  users_who_like_this_tweet = db.relationship('User', secondary=likes_table)

pw_regex = re.compile(r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%^&*()!])[\w\d@#$]{8,}$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register',methods=["POST"])
def register():
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
  if is_valid == True: #see if user already exists, if not, add them
    instance_of_user_with_email = User.query.filter_by(email=request.form['email'].lower())
    if instance_of_user_with_email.scalar() is not None:
      flash('Email already registered. Please login.')
      return redirect('/')
    pw_hash = bcrypt.generate_password_hash(pw)
    #print(pw_hash)
    flash('Successfully added new user!')
    instance_of_user = User(
      first_name = fn,
      last_name = ln,
      email = email,
      password = pw_hash
    )
  
    #make a new user automaically follow themself
    #instance_of_user.users_this_user_follows.append(instance_of_user)
    db.session.add(instance_of_user)
    db.session.commit()
  return redirect('/')

@app.route('/login',methods=["POST"])
def login():
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
    instance_of_user_with_email = User.query.filter_by(email=request.form['email'].lower()).all()
    print(instance_of_user_with_email)
    if len(instance_of_user_with_email)==0:
      flash('Email does not match any registered users. Please register.')
      return redirect('/')
    if len(instance_of_user_with_email)>0:
      if bcrypt.check_password_hash(instance_of_user_with_email[0].password,request.form['password']) == True:
        print('password matched')
        session['user_email'] = email
        session['first_name'] = instance_of_user_with_email[0].first_name
        session['id'] = instance_of_user_with_email[0].id
        return redirect('/success')
      else:
        flash('Password or email is incorrect.')
        return redirect('/')
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
  if 'id' not in session:
    return redirect('/')
  instance_of_user = User.query.get(session['id'])
  print(instance_of_user)
  list_of_tweets_from_session_user = Tweet.query.filter_by(author_id=session['id']).all()
  print(list_of_tweets_from_session_user)
  
  list_of_users_this_user_follows = instance_of_user.users_this_user_follows
  print(list_of_users_this_user_follows)

  list_of_tweets_from_users_followed_by_the_user = list()
  #get a list of tweets from the followed users
  for user in list_of_users_this_user_follows:
    list_of_tweets_from_users_followed_by_the_user += (Tweet.query.filter_by(author_id=user.id))

  all_tweets = list_of_tweets_from_session_user + list_of_tweets_from_users_followed_by_the_user

  #get a count of the likes on the tweets
  for tweet in all_tweets:
    tweet.likes = len(tweet.users_who_like_this_tweet)

  return render_template('dashboard.html',tweets=all_tweets)

@app.route('/get_tweets_mysync/<id>')
def get_tweets_mysync(id):
  return none

@app.route('/tweet/create', methods=["POST"])
def tweet():
  if 'id' not in session:
    flash('You must login to create a tweet')
    return redirect('/')
  is_valid = True
  if len(request.form['tweet'])<1:
    flash('tweet must contain some content')
    is_valid = False
    return redirect('/dashboard')
  new_tweet = Tweet(
    content=request.form['tweet'],
    author_id=session['id']
  )
  print(new_tweet)
  db.session.add(new_tweet)
  db.session.commit()
  return redirect('/dashboard')

@app.route('/add_like/<id>', methods=["POST","GET"])
def add_like(id):
  instance_of_tweet = Tweet.query.get(id)
  instance_of_logged_in_user = User.query.get(session['id'])
  instance_of_logged_in_user.tweets_this_user_likes.append(instance_of_tweet)
  db.session.commit()
  return redirect('/dashboard')

@app.route('/tweets/<id>/delete', methods=["POST"])
def delete_tweet(id):
  instance_of_tweet = Tweet.query.get(id)
  db.session.delete(instance_of_tweet)
  db.session.commit()
  return redirect('/dashboard')

@app.route('/tweets/<id>/edit')
def edit_tweet(id):
  instance_of_tweet = Tweet.query.get(id)
  return render_template('edit_tweet.html', tweet = instance_of_tweet)

@app.route('/tweets/<id>/update', methods=["POST"])
def update_tweet(id):
  if 'id' not in session:
    flash('You must login to create a tweet')
    return redirect('/')
  is_valid = True
  if len(request.form['tweet'])<1:
    flash('tweet must contain some content')
    is_valid = False
    return redirect('/dashboard')
  instance_of_tweet_to_update = Tweet.query.get(id)
  instance_of_tweet_to_update.content = request.form['tweet']
  db.session.commit()
  return redirect('/dashboard')

@app.route('/users')
def show_users():
  list_of_all_users = User.query.all()
  instance_of_user = User.query.get(session['id'])
  list_of_users_this_user_followers = instance_of_user.users_this_user_follows
  for user in list_of_all_users:
    if user in list_of_users_this_user_followers:
      print(user.first_name,"is followed")
      user.is_followed = True
    else:
      user.is_followed = False
  return render_template('/show_users.html', users = list_of_all_users)

@app.route('/follow/<uid>')
def follow(uid):
  #get the logged in user object
  instance_of_logged_in_user = User.query.get(session['id'])
  #get the user object of the person they want to follow
  instance_of_person_to_follow = User.query.get(uid)
  #add the person object to the list of users the logged in user follows
  instance_of_logged_in_user.users_this_user_follows.append(instance_of_person_to_follow)
  db.session.commit()
  return redirect('/users')

@app.route('/unfollow/<uid>')
def unfollow(uid):
  instance_of_logged_in_user = User.query.get(session['id'])
  #get the user object of the person they want to follow
  instance_of_person_to_unfollow = User.query.get(uid)
  #add the person object to the list of users the logged in user follows
  instance_of_logged_in_user.users_this_user_follows.remove(instance_of_person_to_unfollow)
  db.session.commit()
  return redirect('/users')

@app.route("/email", methods=['POST'])
def username():
  found = False
  instance_of_user_with_email = User.query.filter_by(email=request.form['email'].lower()).all()  
  if len(instance_of_user_with_email)>0:
    found = True
  return render_template('partials/email.html', found=found)  # render a partial and return it
  # Notice that we are rendering on a post! Why is it okay to render on a post in this scenario?
  # Consider what would happen if the user clicks refresh. Would the form be resubmitted?

@app.route("/usersearch")
def search():
  instance_of_users_with_name = User.query.filter(User.first_name.like("%"+request.args.get('name')+"%")).all()
  print(instance_of_users_with_name)
  if len(instance_of_users_with_name)>0:
    return render_template("usersearch.html", users = instance_of_users_with_name) # render a template which uses the resu
  else:
    flash("no user with than name")
  return False

if __name__ == "__main__":
  app.run(debug=True)