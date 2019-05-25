#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play():
  return render_template('index.html')


@app.route('/play/<int:x>')
def boxes(x):
  return render_template('index.html',x=x)

@app.route('/play/<int:x>/<color>')
def colors(x,color):
  return render_template('index.html',x=x,html_color=color)


if __name__ == "__main__":
  app.run(debug=True)