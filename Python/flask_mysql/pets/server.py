#! /usr/bin/python3
from flask import Flask, redirect, request, render_template
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
  mysql = connectToMySQL('pets')
  pets = mysql.query_db("Select * from pets;")
  print(pets)
  return render_template('index.html', pets=pets)
    
@app.route('/insert_pet',methods=['POST'])
def insert_pet():
  mysql = connectToMySQL('pets')
  query = "INSERT INTO pets (name, type, created_at,updated_at) values (%(name)s,%(type)s,NOW(),NOW());"
  data = {
    'name': request.form['name'],
    'type': request.form['type']
  }
  mysql.query_db(query,data)
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)
