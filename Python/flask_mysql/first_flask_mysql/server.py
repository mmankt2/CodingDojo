#! /usr/bin/python3

from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL("first_flask")
    friends = mysql.query_db("SELECT * FROM friends;")
    print(friends)
    return render_template("index.html", all_friends = friends)
    
@app.route("/insert", methods = ['POST'])
def insert():
  mysql = connectToMySQL('first_flask')	
  query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) values (%(f)s,%(ln)s,%(occ)s,NOW(),NOW());'
  data = {
    'fn':request.form['first_name'],
    'ln':request.form['last_name'],
    'occ':request.form['occupation']
  }
  id = mysql.query_db(query,data)
  return redirect('/')

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
  print(request.form)
  # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
  #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
  mysql = connectToMySQL('first_flask')	
  query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) values (%(fn)s,%(ln)s,%(occ)s,NOW(),NOW());'
  data = {
    'fn':request.form['fname'],
    'ln':request.form['lname'],
    'occ':request.form['occ']
  }
  id = mysql.query_db(query,data)
  return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
