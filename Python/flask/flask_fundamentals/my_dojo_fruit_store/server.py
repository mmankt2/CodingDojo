#! /usr/bin/python3
from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    
    timestamp = datetime.datetime.now()
    
    currenttime = timestamp.strftime('%B %d %Y %H:%M:%S %p')
    
    num_items = int(request.form['strawberry']) + int(request.form['apple']) + int(request.form['raspberry'])
    
    student_info = {'first':request.form['first_name'], 'last':request.form['last_name'], 'id':request.form['student_id']}
    print(student_info)

    items = { 'strawberry': int(request.form['strawberry']), 'apple': int(request.form['apple']), 'raspberry': int(request.form['raspberry']) }
    print(items)

    return render_template("checkout.html", num_items=num_items, currenttime=currenttime, items=items, student_info=student_info)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    