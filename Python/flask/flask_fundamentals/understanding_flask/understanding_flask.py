#! /usr/bin/python3
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
    
# import statements, maybe some other routes    
@app.route('/dojo')
def dojo():
  return "Dojo!"
    
@app.route('/say/<name>/') # for a route '/say/____' anything after '/say/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<number>/<word>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(number, word):
    number = int(number)
   #  while number >=0:
   #   print(word)
   #   number -= 1 
    return "<p>word</p>"*number

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.