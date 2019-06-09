#! /usr/bin/python3
from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
app = Flask(__name__)

app.secret_key = "super secret"
bcrypt = Bcrypt(app)
db='friends2'

@app.route('/')
def index():
  mysql = connectToMySQL(db)
  query = "SELECT * from friends;"
  results = mysql.query_db(query)
  print(results)
  return render_template('index.html')

@app.route('/users/new')
def new_user():
  mysql = connectToMySQL('friends2')
  query = "SELECT * from friends;"
  results = mysql.query_db(query)
  print(results)
  return render_template('index.html')#redirect('/users/<id>')

@app.route('/users/create', methods=["POST"])
def create_user():
  mysql = connectToMySQL(db)
  query = "INSERT INTO friends (first_name,last_name,email,created_at, updated_at) values (%(fn)s,%(ln)s,%(email)s,NOW(),NOW());"
  data = {
    'fn':request.form['first_name'],
    'ln':request.form['last_name'],
    'email':request.form['email']
  }
  session['id'] = mysql.query_db(query,data)
  print(session['id'])
  id = session['id']
  #print(session['id'])
  return redirect('/users/'+str(id))

@app.route('/users/<id>')
def show_user(id):
  print(session['id'])
  mysql = connectToMySQL(db)
  query = "SELECT * from friends where id = %(id)s;"
  q_data = { 'id':id}
  data = mysql.query_db(query,q_data)
  session['fn'] = data[0]['first_name']
  session['ln'] = data[0]['last_name']
  session['email'] = data[0]['email']
  print(data[0])
  return render_template('show_user.html',data=data[0],id=id)

@app.route('/users/<id>/edit')
def edit(id):
  mysql = connectToMySQL(db)
  query = "SELECT * from friends where id = %(id)s;"
  q_data = { 'id':id}
  data = mysql.query_db(query,q_data)
  return render_template('edit.html',id=id,data=data[0])

@app.route('/users/<id>/update', methods=["POST"])
def update_user(id):
  mysql = connectToMySQL(db)
  query = "UPDATE friends set first_name=%(fn)s, last_name=%(ln)s, email=%(email)s, updated_at=NOW() where id=%(id)s;"
  print(id)
  q_data = {
    'id':id,
    'fn':request.form['first_name'],
    'ln':request.form['last_name'],
    'email':request.form['email']
  }
  mysql.query_db(query,q_data)
  return redirect('/users/'+str(id))

@app.route('/users/<id>/destroy')
def delete(id):
  mysql = connectToMySQL(db)
  query = "DELETE from friends where id=%(id)s;"
  q_data = {'id':id}
  mysql.query_db(query,q_data)
  return redirect('/users')

@app.route('/users')
def users():
  mysql = connectToMySQL(db)
  query = "SELECT * from friends;"
  data = mysql.query_db(query)
  return render_template('users.html', data=data)

if __name__ == "__main__":
  app.run(debug=True)