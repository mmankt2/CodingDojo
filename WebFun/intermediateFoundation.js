//Part 1

//1.Sigma - Implement function sigma(num) that, given a number, returns 
//the sum of all positive integers up to the given number (inclusive).  
//Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).
function sigma(num){
  var sum=0;
  while (num>0){
    sum = sum+num;
    num--;
  }
  return sum;
}
console.log(sigma(5));

//2.Factorial - Write a function factorial(num) that, given a number, 
//returns the product (multiplication) of all positive integers from 1 up 
//to the given number (inclusive).  For example, factorial(3) = 6 (or 
//1*2*3); factorial(5) = 120 (or 1*2*3*4*5).
function factorial(num){
  var answer = num;
  num--;
  while (num>0){
    answer = num*answer;
    num--;
  }
  return answer;
}
console.log(factorial(5));

//3.Fibonacci - Create a function to generate Fibonacci numbers.  In this 
//famous mathematical sequence, each number is the sum of the previous 
//two, starting with values 0 and 1.  Your function should accept one 
//argument, an index into the sequence (where 0 corresponds to the 
//initial value, 4 corresponds to the value four later, etc).  
//Examples: 
//fibonacci(0) = 0 (given), 
//fibonacci(1) = 1 (given), 
//fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), 
//fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), 
//fibonacci(4) = 3 (1+2), 
//fibonacci(5) = 5 (2+3), 
//fibonacci(6) = 8 (3+5), 
//fibonacci(7) = 13 (5+8).  
//Do this without using recursion first.  If you don't know what a 
//recursion is yet, don't worry as we'll be introducing this concept in Part 
//2 of this assignment.
function fibonacci(num){
  var fib0 = 0;
  var fib1 = 1;
  var fibarr=[fib0,fib1];
  for (var i=2;i<=num;i++){
    fibarr.push(fibarr[i-1]+fibarr[i-2]);
  }
  console.log(fibarr[num]);
}
fibonacci(3);

//4.Array: Second-to-Last: Return the second-to-last element of an array. 
//Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return 
//null.
function secToLast(arr){
  if(arr.length<2){
    return null;
  }
  return arr[arr.length-2];
}
console.log(secToLast([42,true,4,"Liam",7]));

//5.Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given 
//([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.
function nthToLast(arr,num){
  if (arr.length<num){
    return null;
  }
  return arr[arr.length-num];
}
console.log(nthToLast([5,2,3,6,4,9,7],3));

//6.Array: Second-Largest: Return the second-largest element of an array. Given 
//[42,1,4,3.14,7], return 7.  If the array is too short, return null.
//IN THIS EXAMPLE, ISN'T THE SECOND LARGEST ELEMENT 14??????????
function secLargest(arr){
  var len = arr.length;
  var max = arr[0];
  var secLar = arr[0];
  
  if (len<2){
    return null;
  }
  //find the max
  for (var i=0;i<len;i++){
    if (arr[i]>max){
      max = arr[i];
    }
  }
  
  //find the second largest
  for (var i=0;i<len;i++){
    if(secLar == max){
      secLar = arr[i+1];
    }
    if(arr[i]<max && arr[i]>secLar){
      secLar=arr[i];
    }
  }
  console.log(secLar);
}

secLargest([42,1,4,3,14,7,18,-3,50]);


//7.Double Trouble: Create a function that changes a given array to list each 
//existing element twice, retaining original order.  Convert 
//[4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].
function double(arr){
  var len = arr.length;
  for (var i = 0;i<len*2;i+=2){
    arrLength = arr.length;
    for (var j = arrLength;j>0+i;j--){
      arr[j]=arr[j-1];
    }
  }
  return arr;
}
doubleArray = double([4, "Ulysses", 42, false,2]);
console.log(doubleArray);

//fibonacci with recursion
function fib(n){
  if (n==1 or n==0){
    return n;
  }

  return fib(n-1)+fib(n-2);
}

console.log(fib(1));