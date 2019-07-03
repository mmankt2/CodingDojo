$(document).ready(function(){
    console.log("working with jquery")
    $('#tweetForm').submit(function create_tweet(e){
        e.preventDefault(); //prevent submission of form
        console.log("made it to the tweetForm submit function")
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/create_tweets",
            data: $("#tweetForm").serialize()   // capture all the data in the form in the variable data
        })
        .done(function(response){
            $('.previous_tweets').prepend(response);
        })
    })  
})