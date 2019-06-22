from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt # this allows us to secure client passwords
import re # this allows us to use regular expressions/patterns

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app) # remember to create an instance of Bcrypt to use
database = 'YOUR SCHEMA NAME HERE'
app.secret_key = 'Super Duper Ultra Top Secret!!' # remember this line, so that you can use session!! Session won't work eithout it

# THIS GET ROUTE DISPLAYS THE LOGIN/REG HTML FILE
@app.route('/')
def signin():
    return render_template("signin.html")

#THIS POST ROUTE WILL PROCESS CLIENT'S FORM DATA FROM THE REGISTRATION FORM
@app.route('/register', methods=['POST'])
def register():
    # first, check if the data is valid  by setting a flag 
    # that remains false for valid data and true for any errors
    is_valid = False

    if len(request.form['first_name']) < 2:
        flash("First name must be at least 2 characters long.")
        is_valid = True
    if len(request.form['last_name']) < 2:
        flash("First name must be at least 2 characters long.")
        is_valid = True
    if not re.match(EMAIL_REGEX,request.form['reg_email']):
        flash("Email address is not valid.")
        is_valid = True
    if len(request.form['reg_password']) < 8:
        flash("Password must be at least 8 characters long.")
        is_valid = True
    elif request.form['reg_password'] != request.form['confirm_password']:
        flash("Passwords do not match.")
        is_valid = True
    
    # if the data is valid, add them to your database and hash the client's password
    # save some client info into session
    # then redirect them to the "success" page
    if is_valid == False:
        pw_hash = bcrypt.generate_password_hash(request.form['reg_password'])  
        mysql = connectToMySQL(database)
        query = "INSERT INTO friends(first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, NOW(), NOW());"
        data = {
            "fn": request.form["first_name"],
            "ln": request.form["last_name"],
            "em": request.form["reg_email"],
            "pw": pw_hash
        }
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id
        session['greeting'] = request.form['first_name']
        return redirect("/success")
    # if data is invalid, redirect back to the "Login/Registration" page
    else:
        return redirect('/')

# THIS POST ROUTE THAT WILL VERIFY CLIENT'S LOGIN CREDENTIALS FROM LOGIN FORM
@app.route('/login', methods=['POST'])
def login():
    # check to see if the email address is already in the database
    mysql = connectToMySQL(database)
    query = "SELECT * FROM users WHERE email = %(em)s"
    data = {
        "em": request.form['log_email']
    }
    result = mysql.query_db(query, data)
    # if it is, then check if he password saved in the database matches the one in form data
    if len(result) > 0:
        if bcrypt.check_password_hash(result[0]['password'], request.form['log_password']): # NOTICE the [0] in this line!!
    # if the email and password match, save some client info into session
    # then send them to the "Success" page
            session['user_id'] = result[0]['id']
            session['greeting'] = result[0]['first_name']
            return redirect('/success')
    # else,send client a flash message
        else:
            flash("Email and password do not match.")
    else:
    # if the email has not been registered yet, send client a flash message
        flash("The email address has not been registered.")
    return redirect('/')

# GET ROUTE WILL DISPLAY SUCCESS PAGE IF THE CLIENT HAS LOGGED IN OR REGISTERED
@app.route('/success')
def success():
    # check if the client has any session data stored
    # if not, redirect back to "Login/Register" page
    if 'user_id' in session:
        return render_template("success.html")
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    pass
    # figure out how to clear session data 
    # and redirect the client back to the "Login/Register" page

if __name__=="__main__":
    app.run(debug=True)