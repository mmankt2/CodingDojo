//Given an array and a value Y, count and print the number of array values greater than Y.
var arr = [1,2,3,4,5];
var y = 4;
var len = arr.length;
var count = 0;
for (var i=0;i<len;i++){
  if(arr[i]>y){
    count+=1;
  }  
}
console.log(count);


//Given an array, print the max, min and average values for that array.
var arr = [1,2,3,4,5,-1,-2,10];
var len = arr.length;
var max = arr[0];
var min = arr[0];
var sum = 0;
for (var i=0;i<len;i++){
  if(arr[i]<min){
    min = arr[i];
  }
  if(arr[i]>max){
    max = arr[i];
  }
  sum+=arr[i];
}
var avg = sum/len;
console.log(max,min,avg);

//Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.   For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].
function replaceNegatives(arr){
  var len = arr.length;
  for(var i=0;i<len;i++){
    if(arr[i]<0){
      arr[i]="Dojo";
    }
  }
  return arr;
}
var arr = [1,2,3,4,5,-1,-2,10];
console.log(replaceNegatives(arr));

//Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array).  For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].
function removeVals(arr,start,end){
  var len = arr.length;
  var newArr = []
  for(var i = 0;i<start;i++){
    newArr.push(arr[i]);
  }
  for(var i=end+1;i<len;i++){
    newArr.push(arr[i]);
  }

  return newArr;
}
var myArr = [20,30,40,50,60,70];
console.log(removeVals(myArr,2,4));
