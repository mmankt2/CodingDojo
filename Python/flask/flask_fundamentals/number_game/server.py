#! /usr/bin/python3
from flask import Flask, render_template,redirect,request, session
import random

app = Flask(__name__)
app.secret_key="secretest key"

@app.route("/")
def main():
  if not "answer" in session:
    print("just got here")
    session["counter"] = 0
    session["answer"]=random.randint(1,100)
  print(session["answer"])
  return render_template("main.html")

@app.route("/destroy_session")
def destroy():
  session.clear()
  return redirect("/")

@app.route("/guess", methods=["POST"])
def guessing():
  session["counter"] += 1
  session['guess']=int(request.form["guess"])
  
  if session['guess'] < session['answer']:
    session['status'] = "Too Low"

  if session['guess'] > session['answer']:
    session['status'] = "Too High"  

  if session['guess'] == session['answer']:
    session['status'] = "Correct"  
    
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)