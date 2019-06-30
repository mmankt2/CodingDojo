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