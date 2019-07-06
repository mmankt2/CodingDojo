$('#sendRequest').click(function(){         // the .click() method accepts a callback
  $.ajax({                                
      url: "/friends",
      method: "GET"
  })
  .done(function(res){                    // the .done() method accepts a callback
      $('#game').hide();                     
      $('#result').html(res);             
  })
  $('#game').show();                      
})

$('#sendRequest').click(function(){         // Step 1 - a click happens
  $.ajax({                                // Step 2 - make an AJAX get request to /friends
      url: "/friends",
      method: "GET"
  })
  .done(function(res){                    // Step 4 - receive the response
      $('#game').hide();                  // Step 5 - hide the game   
      $('#result').html(res);             // Step 6 - manipulate the html to display the data from the server
  })
  $('#game').show();                      // Step 3 - show the game to occupy the user while waiting
})
//########################################
//templates/wall.html
<html>
    <head>
        <script src="{{ url_for('static', filename='wall.js') }}"></script>
    </head>
    <form action="/register" method="post" id="regForm">
        <div id="usernameMsg"></div>   <!-- notice the empty div reserved for our message -->
        <input id="username" type="text">
        <button type="submit">Submit</button>
    </form>
</html>

//#static/wall.js
$(document).ready(function(){
    $('#username').keyup(function(){
        var data = $("#regForm").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/username",
            data: data
        })
        .done(function(res){
             $('#usernameMsg').html(res)  // manipulate the dom when the response comes back
        })
    })
})

//server.py
@app.route("/username", methods=['POST'])
def username():
    found = False
    mysql = connectToMySQL('ajaxWall')        # connect to the database
    query = "SELECT username from users WHERE users.username = %(user)s;"
    data = { 'user': request.form['username'] }
    result = mysql.query_db(query, data)
    if result:
        found = True
    return render_template('partials/username.html', found=found)  # render a partial and return it
    # Notice that we are rendering on a post! Why is it okay to render on a post in this scenario?
    # Consider what would happen if the user clicks refresh. Would the form be resubmitted?

//templates/partials/username.html
{% if found == True %}
<p class="error">Username has been taken.</p>
{% endif %}
{% if found == False %}
<p class="success"> This username is available</p>
{% endif %}


//when using a GET method, localhost:5000/users?name=kermit&color=green
@app.route('/users')
def data_from_query_string():
    print(request.args.get('name'))     # outputs kermit
    print(request.args.get('color'))    # outputs green
    # any other logic goes here

//general ajax call
$('#form1').submit(function(){
  $.ajax({ 
    method: "POST",     // using a GET request would put your form data in the url as query strings
    url: $(this).attr('action'), // 'this' refers to #form1, the element that triggered the function
    data: $(this).serialize()
  })
  .done(function(response) {
    // your code on what to do once the http response is received
  })
  .fail(function(response) {
    // optional code on what to do if the http request fails
  })
  .always(function(data){
    // optional code on what should be done regardless of whether the http request is successful or not
  })
  return false; // return false so the form is not submitted normally
});

//serializing in pythong to create JSON data
import json
# python types must be converted to json using the json module
my_list = [
    {
        "first_name": "Wes",
        "last_name": "Harper",
        "email": "wharper@codingdojo.com",
    }
]
my_jsonified_list = json.dumps(my_list)<br>

//add this to config.py
from flask_marshmallow import Marshmallow
# this was already here
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# this is new
ma = Marshmallow(app)<br>

//do this in models file
from config import db, ma
class SomeModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # the rest omitted for brevity
class SomeModelSchema(ma.ModelSchema):
    class Meta:
        model = SomeModel

//do this in the controller file
# conveniently, Flask has a jsonify function
from flask import render_template, request, redirect, session, url_for, flash, jsonify
from server.models.some_model import SomeModel, SomeModelSchema
def one():
    one_item = SomeModel.query.first()
    some_schema = SomeModelSchema()
    output = some_schema.dump(one_item).data
    return jsonify({"some_item": output})
def all():
    items = SomeModel.query.all()
    some_schema = SomeModelSchema(many=True) # this is different!
    output = some_schema.dump(items).data
    return jsonify({"some_item": output})