var world = [
  [2,2,2,2,2,2,2,2,2,2],
  [2,0,1,1,1,1,1,1,1,2],
  [2,1,2,1,1,1,1,1,1,2],
  [2,1,2,1,2,2,2,2,1,2],
  [2,1,2,1,2,1,1,1,1,2],
  [2,1,2,1,2,1,2,2,2,2],
  [2,1,2,2,2,1,1,1,1,2],
  [2,1,1,1,1,1,2,1,1,2],
  [2,1,1,1,1,1,2,1,1,2],
  [2,2,2,2,2,2,2,2,2,2]
];

var score = 0;

var pacman = {
  x:1,
  y:1
}

var ghost = {
  x:5,
  y:5
}

function displayWorld(){
  var output='';

  for (var i=0;i<world.length;i++){
    output += '<div class="row">';

    for (var j=0;j<world[i].length; j++){
      if(world[i][j]==2){
        output += '<div class="brick"></div>';
      }
      else if (world[i][j]==1){
        output += '<div class="coin"></div>';
      }
      else if (world[i][j]==0){
        output += '<div class="empty"></div>';
      }
      else if (world[i][j]==3){
        output += '<div class="cherry"></div>';
      }
    }
    output += '</div>';   
  }
  //console.log(output);
  document.getElementById('world').innerHTML=output;
}

function displayPacman(){
  document.getElementById('pacman').style.left = pacman.x*20 + "px";
  document.getElementById('pacman').style.top = pacman.y*20 + "px";
}

function displayScore(){
  document.getElementById('score').innerHTML = score;
}

function displayCherry(){
  world[4][4]=3;
  displayWorld();
}

function displayGhost(){
  var x = ghost.x;
  var y = ghost.y;
  ghost.x += Math.floor((Math.random()*3)-1);
  if (world[ghost.y][ghost.x]==2||ghost.x>world[0].length||ghost.x<1){
    ghost.x=x;
    return;
  }
  document.getElementById('ghost').style.left = ghost.x*20 + "px";
  document.getElementById('ghost').style.top = ghost.y*20 + "px";
  displayWorld();

  ghost.y += Math.floor((Math.random()*3)-1);
  if (world[ghost.y][ghost.x]==2||ghost.y>world.length||ghost.y<1){
    ghost.y=y;
    return;
  }

  document.getElementById('ghost').style.left = ghost.x*20 + "px";
  document.getElementById('ghost').style.top = ghost.y*20 + "px";
  displayWorld();
  if (pacman.x == ghost.x && pacman.y==ghost.y){
    document.getElementById('pacman').style.backgroundImage = 'url("dying2.gif")';
    document.getElementById('pacman').style.backgroundSize = 'cover';
    document.getElementById('game_over').style.display = 'inline-block';
    setTimeout(function(){location.reload();},1000);
  }
}

setInterval(function(){ displayCherry() },5000);
setInterval(function(){displayGhost()},200);

document.onkeydown = function(e){
  //console.log(e.keyCode);
  if (e.keyCode==37){
    pacman.x--;
    document.getElementById('pacman').style.transform = "scaleX(-1)";
    if(world[pacman.y][pacman.x]==2){
      pacman.x++;
      return;
    }
  }
  if (e.keyCode==39){
    pacman.x++;
    document.getElementById('pacman').style.transform = "scaleX(1)";
    if(world[pacman.y][pacman.x]==2){
      pacman.x--;
      return;
    }
  }
  if (e.keyCode ==38){
    pacman.y--;
    document.getElementById('pacman').style.transform = "rotate(-90deg)";
    if(world[pacman.y][pacman.x]==2){
      pacman.y++;
      return;
    }
  }
  if (e.keyCode ==40){
    pacman.y++;
    document.getElementById('pacman').style.transform = "rotate(90deg)";
    if(world[pacman.y][pacman.x]==2){
      pacman.y--;
      return;
    }
  }
  if (pacman.x == ghost.x && pacman.y==ghost.y){
    document.getElementById('pacman').style.backgroundImage = 'url("dying2.gif")';
    document.getElementById('pacman').style.backgroundSize = 'cover';
    document.getElementById('game_over').style.display = 'inline-block';
    setTimeout(function(){location.reload();},1000);
  }

  displayPacman();

  if (world[pacman.y][pacman.x]==1){
    world[pacman.y][pacman.x]=0;
    score+=10;
    displayScore();
    displayWorld();
  }

  if (world[pacman.y][pacman.x]==3){
    world[pacman.y][pacman.x]=0;
    score+=50;
    displayScore();
    displayWorld();
  }
}

displayCherry();
displayWorld();
displayPacman();
displayScore();
displayGhost();