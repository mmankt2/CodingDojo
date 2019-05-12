$(document).ready(function(){
  var num_sprites = 15;
  //console.log('in js');
  
  var img_string = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/';
  var img_api_string='http://pokeapi.co/api/v2/pokemon/';
  
  var html_string="";

  for (var i=0;i<=num_sprites;i++){
    html_string+="<img id="+i+" src="+img_string+i+".png>";
  }

  $('#sprites').append(html_string);


  $('#sprites img').on('click',function(){
    $('#pokedex').html('');
    var image_id = $(this).attr('id');
    //console.log(image_id);
    var image_src = $(this).attr('src');
    var types_html = "<h4>Types</h4>";
    types_html+="<ul>";

    $.get(img_api_string+image_id,function(data){
      console.log('in .get');
      var pokename=data.name;
      var pokeheight=data.height;
      var pokeweight=data.weight;

      for (var i=0;i<data.types.length;i++){
        types_html+="<li>"+data.types[i].type.name+"</li>";
        console.log(types_html);
      }

      types_html+="</ul>";
      console.log(types_html);

      $('#pokedex').append('<h2>'+pokename+'</h2>');
      $('#pokedex').append('<img src='+image_src+'>');
      $('#pokedex').append(types_html);
      $('#pokedex').append('<h4>Height</h4><p>'+pokeheight+'</p>');
      $('#pokedex').append('<h4>Weight</h4><p>'+pokeweight+'</p>');

    }, "json");
    
    //console.log(image_src);
    
  })

})