//To Do 1
//recursive sigma
function rSigma(num){
  //base case
  if (num == 1||num ==0){
    return num;
  }
  if (num < 0 ){
    return 0;
  }

  return num + rSigma(num - 1);
}
console.log(rSigma(-1));

//recursive factorial
function rFactorial(num){
  num = Math.floor(num);
  
  //base case
  if (num <= 1){
    return 1;
  }

  return num * rFactorial(num - 1);
}
console.log(rFactorial(6.6));

//floor fill
function floodFill(canvas,startXY,newColor,oldColor){
  x = startXY[0];
  y = startXY[1];
  currentColor = canvas[y][x];

  if (oldColor == undefined){
    oldColor = currentColor;
  }
  
  //if the current color is the not same as the old color, do nothing
  if(currentColor !== oldColor){
    return;
  }

  //do your function
  canvas[y][x] = newColor;
  
  if(x+1 < canvas[0].length){
    floodFill(canvas,[x+1,y],newColor,oldColor);
  }
  if(x-1 >= 0){
    floodFill(canvas,[x-1,y],newColor,oldColor);
  }
  
  if(y+1 < canvas.length){
    floodFill(canvas,[x,y+1],newColor,oldColor);
  }
  if(y-1 >= 0){
    floodFill(canvas,[x,y-1],newColor,oldColor);
  }
  return canvas;
}
const canvas = [
  [3,3,3,3,3],
  [3,3,3,3,3],
  [3,2,3,4,3],
  [2,3,3,4,0],
  [7,3,3,5,3],
  [6,5,3,4,1],
  [1,2,3,3,3]
];
startXY = [3,2];
newColor = 10;
console.log(canvas);
console.log(floodFill(canvas, startXY, newColor));
