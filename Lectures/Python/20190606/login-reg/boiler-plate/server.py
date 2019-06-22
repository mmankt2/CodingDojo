# make sure you import EVERYTHING you need!!
# don't forget bcrypt and re
from flask import Flask
from mysqlconnection import connectToMySQL


app = Flask(__name__)
# remember to create an instance of Bcrypt to use
database = 'YOUR SCHEMA NAME HERE'
# don't forget a secret key

# THIS GET ROUTE DISPLAYS THE LOGIN/REG HTML FILE
@app.route('/')
def signin():
    # render the signin.html file

#THIS POST ROUTE WILL PROCESS CLIENT'S FORM DATA FROM THE REGISTRATION FORM
@app.route('/register', methods=['POST'])
def register():
    is_valid = False # first, check if the data is valid by setting a flag
                     # that remains false for valid data and true for any errors

    if len(request.form['first_name']) < 2:
        flash("First name must be at least 2 characters long.")
        is_valid = True
    # FINISH THIS VALIDATION!! 
        # 1. First Name and Last Name should be at least 2 characters long
        # 2. Check that the email address is valid with a REGEX
        # 3. Check that the valid email address is not already registered in the database
        # 4. Password must be at least 8 characters long
        # 5. Password and Confirm Password must match
    
    # if the data is valid, 
    if is_valid == False:
        # add them to your database and hash the client's password
        # save some client info into session
        # then redirect them to the "success" page
    # else,
    else:
        # redirect back to the "Login/Registration" page

# THIS POST ROUTE THAT WILL VERIFY CLIENT'S LOGIN CREDENTIALS FROM LOGIN FORM
@app.route('/login', methods=['POST'])
def login():
    # check to see if the email address is already in the database
    
    # if it is, then check if he password saved in the database matches the one in form data
    
        # if the email and password match, save some client info into session
        # then send them to the "Success" page
            
        # else,send client a flash message

    # if the email has not been registered yet, send client a flash message
        

# GET ROUTE WILL DISPLAY SUCCESS PAGE IF THE CLIENT HAS LOGGED IN OR REGISTERED
@app.route('/success')
def success():
    # if the client has any session data stored
        # render success.html file
    # else, 
        # redirect back to "Login/Register" page

@app.route('/logout')
def logout():
    # figure out how to clear session data 
    # and redirect the client back to the "Login/Register" page

if __name__=="__main__":
    app.run(debug=True)