//Return the given array, after setting any negative values to zero.  For example resetNegatives( [1,2,-1, -3]) should return [1,2,0,0].
function resetNegatives(arr){
  var len = arr.length;
  for(var i=0;i<len;i++){
    if(arr[i]<0){
      arr[i]=0;
    }
  }
  return arr;
}
var myArr=[1,2,-1,-3];
console.log(resetNegatives(myArr));

//Given an array, move all values forward by one index, dropping the first and leaving a ‘0’ value at the end.  For example moveForward( [1,2,3]) should return [2,3,0].
function moveForward(arr){
  var arrLength=arr.length;
  for(var i=0;i<arrLength-1;i++){
    arr[i]=arr[i+1];
  }
  arr[arrLength-1]=0;
  return arr;
}
console.log(moveForward([1,2,3]));

//Given an array, return an array with values in a reversed order.  For example, returnReversed([1,2,3]) should return [3,2,1].
function returnReversed(arr){
  var arrLength=arr.length;
  var halfLength=arrLength/2;
  for(var i=0;i<halfLength;i++){
    var hold = arr[i];
    arr[i]=arr[arrLength-1-i];
    arr[arrLength-1-i]=hold;
  }
  return arr;
}
console.log(returnReversed([1,2,3]));

//Create a function that changes a given array to list each original element twice, retaining original order.  Have the function return the new array.  For example repeatTwice( [4,”Ulysses”, 42, false] ) should return [4,4, “Ulysses”, “Ulysses”, 42, 42, false, false].
function repeatTwice(arr){
  var arrLength = arr.length;
  var arrTwice = [];
  for (var i=0;i<arrLength;i++){
    arrTwice[i*2]=arr[i];
    arrTwice[i*2+1]=arr[i];
  }
  return arrTwice;
}
console.log(repeatTwice([4,"Ulysses",42,false]));