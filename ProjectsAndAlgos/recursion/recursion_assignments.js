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
  if(y+1 < canvas.length){
    floodFill(canvas,[x,y+1],newColor,oldColor);
  }
  if(x-1 >= 0){
    floodFill(canvas,[x-1,y],newColor,oldColor);
  }
  if(y -1 >= 0){
    floodFill(canvas,[x,y-1],newColor,oldColor);
  }
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
startXY = [2,2];
newColor = 10;
console.log(canvas);
console.log(floodFill(canvas, startXY, newColor));

//To Do 3
//Recursive binary search
function rBinarySearch(arr,value,index){
  if (index == undefined){
    index = 0;
  }
  if(arr[index] == value){
    return true;
  }

  index = index + 1;
  if (index <= arr.length){
    return rBinarySearch(arr,value,index);
  }
  
  if (index >= arr.length-1){
    return false;
  }
}
console.log(rBinarySearch([1,3,5,6],4));

//greatest common factor
function rGCF(num1,num2){
  if(num1 == num2){
    return num1;
  }
  if(num1 > num2){
    return rGCF(num1-num2,num2);
  }
  if(num2 > num1){
    return rGCF(num1,num2-num1);
  }
}
console.log(rGCF(25689,987654));

//tarai
function tarai(x,y,z){
  if (x <= y){
    return y;
  }
  else {
    return tarai(tarai(x-1,y,z),tarai(y-1,z,x),tarai(z-1,x,y));
  }
}
//console.log(tarai(10,2,9));

//string: in-order subsets
function strSubsets(string,array,index,substring){
  if(array == undefined){
    array = [];
  }
  if (index ==undefined){
    index = 0;
  }
  if (substring ==undefined){
    substring = "";
  }
  array.push(substring);
  substring += string[index];
  index += 1;

  if (index <= string.length){
    return strSubsets(string,array,index,substring);
  }
  return array;
}
console.log(strSubsets("abc"));