$(document).ready(function(){
  var num_sprites = 151;
  //console.log('in js');
  
  var img_string = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/'
  
  for (var i=0;i<=num_sprites;i++){
    $('#sprites').append("<img src="+img_string+i+".png>");
  }

})