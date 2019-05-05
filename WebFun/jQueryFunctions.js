$(document).ready(function(){

  console.log('You are now working with jQuery');
  
  $('div#toggle button').click(function(){
    console.log('toggle');
    $('div#toggle h2,div#toggle p').toggle();
  });

  $('div#hide button').click(function(){
    console.log('hide');
    $('div#hide h2, div#hide p').hide();
  });

  
  $('div#show button').click(function(){
    console.log('show');
    $('div#hide h2, div#hide p').show();
  });

  $('div#slideDown button').click(function(){
    console.log('slideDown');
    $('div#slideUp p').slideDown("slow");
  });

  $('div#slideUp button').click(function(){
    console.log('slideUp');
    $('div#slideUp p').slideUp("slow");
  });

  $('div#slideToggle button').click(function(){
    console.log('slideToggle');
    $('div#slideToggle img').slideToggle("slow");
  });

  $('div#fadeIn button').click(function(){
    console.log('fadeIn');
    $('div#fadeOut p').fadeIn("slow");
  });

  $('div#fadeOut button').click(function(){
    console.log('fadeOut');
    $('div#fadeOut p').fadeOut("slow");
  });

  $('div#addClass button').click(function(){
    console.log('addClass');
    $('h2').addClass('rainbow');
  });

  $('div#before button').click(function(){
    console.log('before');
    $('h1').before('<h1>Melissa</h1>');
  });

  $('div#after button').click(function(){
    console.log('after');
    $('h1').after('<h1>Littleton</h1>');
  });

  $('div#append button').click(function(){
    console.log('append');
    $('div#append p').append('>>.append adds HTML');
  });
  
  $('div#html button').click(function(){
    console.log('html');
    $('div#html p').html('.html changes the html in a tag');
  });

  $('div#attr button').click(function(){
    console.log('attr');
    $('div#slideToggle img').attr('src','../WebFun/pacman/pacman.gif');
  });
  
  function displayVal(){
    var vals = $('#val select').val();
    $('#val #selection').html('Selection = '+ vals);  
  }
  $('select').change(displayVal)
  
  $('div#text button').click(function(){
    console.log('text');
    $('div#text p').text('<p>.text changes the text inside a tag even though I added p tags</p>');
  });

});//end of document ready