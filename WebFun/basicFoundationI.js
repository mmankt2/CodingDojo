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

console.log(sumArray([1,2,5]));