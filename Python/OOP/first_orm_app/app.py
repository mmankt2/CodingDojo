#! /home/melissa/my_environments/py3SQLAlchemyEnv/bin/python
from flask import Flask, render_template,request,redirect			# same as beforecopy
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first_orm_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key = True)
  first_name = db.Column(db.String(45))
  last_name = db.Column(db.String(45))
  email = db.Column(db.String(45))
  age = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, server_default=func.now())
  updated_at = db.Column(db.DateTime, server_default=func.now())

class Tweets(db.Model):
  __tablename__ = "tweets"
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.Text)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  author = db.relationship('users', foreign_keys=[author_id], backref="user_tweets", cascade="all")

@app.route("/")
def index():
  #to display all users as a list
  list_of_all_users_as_user_instances = User.query.all()
  all_users = list_of_all_users_as_user_instances
  return render_template('index.html', all_users = all_users)

@app.route("/add_user", methods=['POST'])
def register():
  instance_of_user = User(
    first_name = request.form['first_name'],
    last_name = request.form['last_name'],
    email = request.form['email'],
    age = request.form['age']
    )
  print(instance_of_user)
  db.session.add(instance_of_user)
  db.session.commit()
  return redirect('/')

#below are just notes about how to query the user table
@app.route('/show_users')
def show_users():
  #to display all users as a list
  list_of_all_users_as_user_instances = User.query.all()
  #to define which users to display
  all_user_instances_with_bruce_email = User.query.filter_by(email="bruce@dog.com")
  any_users_named_bruce_dog = User.query.filter_by(first_name="Bruce", last_name="Dog")
  #filter by ID
  single_user_instance_with_id_7 = User.query.get(7)

  #updating a db row
  user_instance_to_update = User.query.get(8)
  user_instance_to_update.email = "new@email.com"
  user_instance_to_update.first_name = "George"
  db.session.commit()

  #to delete a row
  user_instance_to_delete = User.query.get(13)
  db.session.delete(user_instance_to_delete)
  db.session.commit()

  return redirect("/")

#this route is just my notes from ORM Queries with Relationships
@app.route('/create_tweet')
def tweet():
  #author_id is the foreign key
  new_tweet = Tweet(content="my first tweet!", authod_id=1)

  #get one user
  single_user = User.query.get(1)
  #get a list of the users tweets
  list_of_user_tweets = single_user.user_tweets
  #to get a single tweet
  single_tweet = Tweet.query.get(1)
  #get the author of the tweet
  tweet_author = single_tweet.author
  #get the first name
  tweet_author_first_name = single_tweet.author.first_name
  tweet_author_last_name = single_tweet.author.last_name

  #to reassign the author of a tweet
  a_tweet = Tweet.query.get(1)
  a_tweet.author_id = 3
  db.session.commit()

  #to delete
  tweet_to_delete = Tweet.query.get(1)
  db.session.delete(tweet_to_delete)
  db.session.commit()
  user_to_delete = User.query.get(1)
  db.session.delete(user_to_delete)
  db.session.commit()



if __name__ == "__main__":
  app.run(debug=True)