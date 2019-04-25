//1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function upToNum(a,b){
  var arr = [];
  if (b<a){
    console.log("a must be less than b");
    return;
  }
  while (a <= b){
    arr.push(a);
    a++;
  }
  return arr;
}
var myArr=upToNum(1,255);
var myArr2=upToNum("1","255");
console.log(myArr);

//2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
function getEvenSum(){
  var b = 1000;
  var sum = 0;
  for (var i = 2; i<=b;i+=2){
    sum +=i;
  }
  return sum;  
}
console.log(getEvenSum());

//3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
function sumOdd(){
  var sum = 0;
  for (var i = 1;i<=4999;i+=2){
    sum += i;
  }
  return sum;
}
console.log(sumOdd());

//4.Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
function sumArray(arr){
  var arrLength = arr.length;
  var sum = 0;
  if(arrLength < 1){
    console.log("arr must have length greater than 0")
    return;
  }
  for(var i = 0;i<arrLength;i++){
    sum += arr[i];
  }
  return sum;
}
console.log(sumArray([1,2,5]));//8

//5.Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
function findMax(arr){
  var max = arr[0];
  var arrLength = arr.length;
  for (var i = 0;i<arrLength;i++){
    if(arr[i]>max){
      max = arr[i];
    }
  }
  return max;
}
console.log(findMax([-3,3,5,7]));

//6.Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
function findAvg(arr){
  var arrLength = arr.length;
  var sum = 0;
  var avg = 0;
  if(arrLength < 1){
    console.log("arr must have length greater than 0")
    return;
  }
  for(var i = 0;i<arrLength;i++){
    sum += arr[i];
  }
  avg = sum/arrLength;
  return avg;
}
console.log(findAvg([1,3,5,7,20]));

//7.Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
function arrOdd(){
  var a = 1;
  var b = 50;
  var arr = [];
  while (a<b){
    arr.push(a);
    a+=2;
  }
  return arr;
}
console.log(arrOdd());

//8.Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
function greaterThanY(arr,y){
  var arrLength = arr.length;
  var count = 0;
  for (var i=0;i<arrLength;i++){
    if(arr[i]>y){
      count++;
    }
  }
  return count;
}
console.log(greaterThanY([1,3,5,7],3));

//9.Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
function squares(arr){
  var arrLength = arr.length;
  for (var i = 0; i<arrLength;i++){
    arr[i] = arr[i]*arr[i]*;
  }
  return arr;
}
console.log(squares([1,5,10,-2]));

//10.Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
function negatives(arr){
  var arrLength = arr.length;
  for (var i = 0; i<arrLength;i++){
    if(arr[i] <0){
      arr[i]=0;
    }
  }
  return arr;
}
console.log(negatives([1,5,10,-2]));

//11.Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
function maxMinAvg(arr){
  var arrLength = arr.length;
  var sum = 0;
  var avg = 0;
  var max = arr[0];
  var min = arr[0];
  for (var i = 0;i<arrLength;i++){
    sum += arr[i];
    if (arr[i]>max){
      max = arr[i];
    }
    if (arr[i]<min){
      min = arr[i];
    }
  }
  avg = sum/arrLength;
  var arrResult=[max,min,avg];
  return arrResult;

}
console.log(maxMinAvg([1,5,10,-2]));

//12.Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
function swap(arr){
  var arrLength=arr.length;
  var temp = arr[0];
  arr[0]=arr[arrLength-1];
  arr[arrLength-1]=temp;
  return arr;
}
console.log(swap([1,5,10,-2]));

//13.Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].
function numToString(arr){
  var arrLength = arr.length;
  for (var i = 0; i<arrLength;i++){
    if(arr[i] <0){
      arr[i]="Dojo";
    }
  }
  return arr;
}
console.log(numToString([-1,-3,2]));