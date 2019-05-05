$(document).ready(function(){

  console.log('You are now working with jQuery');
  
  $('img').click(function(){
    console.log('clicked image');
    $(this).hide();
  });

  var grid = [
    [1,1,1,1],
    [1,1,1,1]
  ];

  function displayPage(){
    var output='';
  
    for (var i=0;i<grid.length;i++){
      output += '<div class="row">';
  
      for (var j=0;j<grid[i].length; j++){
        if(grid[i][j]==1){
          output += '<div class="ninja"></div>';
        }
        else if (grid[i][j]==0){
          output += '<div class="hide"></div>';
        }
      }
      output += '</div>';   
    }
    console.log(output);
    $('#grid').html(output);
  }

  displayPage();


  $('div.row div').click(function(){
    console.log('clicked div.row div');
    $(this).css('background-image','none');
  });

  $('button').click(function(){
    $('div.row div').css('background-image','url("disappearingNinja.jpg")');
  }); 

});//end of document ready