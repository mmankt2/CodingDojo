//recusion
//1. need base case, when we stop recurssing
//2. forward progress
//3. function calls itself

//To Do 1
//print contents of array
function printArray(array){
  for (var index = 0; index < array.length; index++){
    console.log(array[index])
  }
}

function rPrintArray(array,index){
  if(index ===undefined){
    index = 0;
  }
  //base case
  if(index >= array.length){
    return;
  }
  //function purpose
  console.log(array[index]);
  //recursion -> forward progress
  rPrintArray(array,index+1);
}

rPrintArray([1,2,3,4,5,6,7,8])

//recursive sigma
function rSigma(num){
  
  if (num < 0){
    return 0;
  }

  return rSigma(num-1)+ Math.floor(num);
}

//recursive factorial
function rFactorial(num){
  if(num < 0){
    return 0;
  }
  if(num <=0){
    return 1;
  }

  return rFactorial(num-1)*Math.floor(num);
}

//flood fill
const canvas = [
  [3,2,3,4,3],
  [2,3,3,4,0],
  [7,3,3,5,3],
  [6,5,3,4,1],
  [1,2,3,3,3]
]
function floodFill(matrix,startXY,newColor,oldColor){
  const x = startXY[0];
  const y = startXY[1];
  const currentColor = matrix[y][x];
  //set old color on first run
  if(oldColor===undefined){
    oldColor = currentColor;
  }

  if (currentColor !== oldColor){
    return;
  }

  matrix[y][x] = newColor;

  //forward progress, recursion
  if(x+1<matrix[y].length){
    floodFill(matrix,[x+1,y],newColor,oldColor);
  }
  if(x-1>=0){
    floodFill(matrix,[x-1,y],newColor,oldColor);
  }
  if(y+1<matrix.length){
    floodFill(matrix,[x,y+1],newColor,oldColor);
  }
  if(y-1>=0){
    floodFill(matrix,[x,y-1],newColor,oldColor);
  }
  

}
console.log(floodFill(canvas,[2,2],9));