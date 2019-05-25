#! /usr/bin/python3
from flask import Flask, render_template,redirect,request, session
app = Flask(__name__)
app.secret_key="secretest key"

@app.route("/")
def main():
  if not "answer" in session:
    print("just got here")
    session["answer"]=45
  print(session["answer"])
  return render_template("main.html", status="GUESS YO!")

@app.route("/bob", methods=["POST"])
def bob():
  guess=request.form["guess"]
  print(guess)
  session["answer"]+=1
  return redirect("/")


if __name__ == "__main__":
  app.run(debug=True)