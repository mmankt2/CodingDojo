#! /usr/bin/python3
from flask import Flask, render_template,redirect,request, session
import random

app = Flask(__name__)
app.secret_key="secretest key"

@app.route("/")
def main():
  if not "answer" in session:
    print("just got here")
    session["answer"]=random.randint(1,10)
  print(session["answer"])
  return render_template("main.html")

@app.route("/guess", methods=["POST"])
def guessing():
  guess=int(request.form["guess"])
  if guess < session['answer']:
    status = "too low"
  if guess > session['answer']:
    status = "too high"  
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)