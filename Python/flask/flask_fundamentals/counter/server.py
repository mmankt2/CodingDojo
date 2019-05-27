#! /usr/bin/python3
from flask import Flask, render_template,redirect,request, session
import random

app = Flask(__name__)
app.secret_key="secretest key"

@app.route("/")
def main():
  if not "count" in session:
    print("just got here")
    session["count"]=1
  else:
    session["count"] += 1
  print(session["count"])
  return render_template("main.html")

@app.route("/destroy_session")
def destroy():
  session.clear()
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)