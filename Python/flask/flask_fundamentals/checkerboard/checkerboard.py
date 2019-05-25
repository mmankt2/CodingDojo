#! /usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
  return render_template('checkerboard.html')

@app.route('/<int:x>')
def checkerboard_data(x):
  return render_template('checkerboard.html', x=x)


if __name__ == "__main__":
  app.run(debug=True)