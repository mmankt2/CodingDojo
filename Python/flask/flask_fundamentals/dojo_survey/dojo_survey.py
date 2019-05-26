#! /usr/bin/python3
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
  return render_template('dojo_survey.html')

@app.route('/result', methods=['POST'])
def result():
  print(request.form)
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  return render_template('dojo_result.html', name=name, location=location, language=language, comment=comment)

if __name__ == "__main__":
  app.run(debug = True)