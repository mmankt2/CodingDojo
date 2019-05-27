#! /usr/bin/python3
from flask import Flask, render_template,redirect,request, session
import random, datetime

app = Flask(__name__)
app.secret_key="secretest key"

@app.route("/")
def main():
  return render_template("main.html")

@app.route("/process_money", methods=['POST'])
def money():
  if not 'gold' in session:
    session['gold'] = 0
    session['message'] = ""
  if request.form['building'] == "farm":
    gain = random.randint(10,20)
    session['gold'] += gain
  if request.form['building'] == "cave":
    gain = random.randint(5,10)
    session['gold'] += gain
  if request.form['building'] == "house":
    gain = random.randint(2,5)
    session['gold'] += gain
  if request.form['building'] != "casino":
    session['message'] += "<p id='win'>Earned " + str(gain) + " golds from the " + request.form['building'] + "! (" + str(datetime.datetime.now()) + ")</p>"
  if request.form['building'] == "casino":
    gain = random.randint(-50,50)
    session['gold'] += gain
    if gain < 0:
      session['message'] += "<p id='loss'>Entered a casino and lost " + str(gain) + " golds... Ouch.. (" + str(datetime.datetime.now()) + ")</p>"
    else:
      session['message'] += "<p id='win'>Earned " + str(gain) + " golds from the casino! (" + str(datetime.datetime.now()) + ")</p>"

  return redirect("/")

@app.route("/destroy_session")
def destroy():
  session.clear()
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)