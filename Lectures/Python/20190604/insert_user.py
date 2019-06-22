from flask import Flask, render_template, request, redirect, session, flash 
from datetime import datetime 
from mysqlconnection import connectToMySQL
app = Flask(__name__)
"""
C - create
R - read
U - update
D - delete
"""
@app.route('/')
def index():
  query = "SELECT id, first_name, last_name, email, created_at FROM my_users"
  mysql = connectToMySQL('users')
  list_of_users = mysql.query_db(query)
  print(list_of_users)
  return render_template("insert_user.html", users=list_of_users)

@app.route('/insert_user', methods=['POST'])
def save_user_to_db(): #CREATE
  #print(request.form["first_name"])
  #print(request.form["last_name"])
  #print(request.form["email"])

  query = "INSERT INTO my_users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(e)s, NOW(),NOW())"
  data = {
    'fn':request.form['first_name'],
    'ln':request.form['last_name'],
    'e':request.form['email']
  }

  mysql = connectToMySQL('')
  user_id = mysql.query_db(query, data)
  print(user_id)
  return redirect('/')

@app.route('/delete/user/<id>')
def delete_user(user_id):
  print(user_id)
  query = "DELETE from my_users where id = %(id)s;"
  data = {
    'id':user_id
  }
  mysql = connectToMySQL('users')
  list_of_users = mysql.query_db(query, data)
  return redirect("/")


if __name__ == "__main__":
  app.run(debug=True)