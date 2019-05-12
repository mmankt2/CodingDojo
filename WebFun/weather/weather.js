$(document).ready(function() {
  console.log('working in js');
  $('form').submit(function() {

    console.log('submitted');
    console.log($('#city').val());

    var city = $('#city').val();
    var url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=90a5eebd6d3fafdb10eaec2a0e2ddeee"
    // your code here (build up your url)
      
    $.get(url, function(res) {
      // your code here
      $('#weather_info').html('')
      var tempK = res.main.temp;
      var tempF = ((tempK-273.15)*1.8)+32;
      tempF = Math.round(tempF);
      $('#weather_info').html('<h2>'+city+'</h2><h4>Temperature: '+tempF+' F</h4>');
    }, 'json');
    // don't forget to return false so the page doesn't refresh
    return false;
  });
});
