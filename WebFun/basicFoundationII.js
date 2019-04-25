//1.Biggie Size - Given an array, write a function that changes all 
//positive numbers in the array to the string "big".  Example: 
//makeItBig([-1,3,5,-5]) returns that same array, changed to 
//[-1, "big", "big", -5].
function makeItBig(arr){
  var arrLength=arr.length;
  for (var i=0;i<arrLength;i++){
    if(arr[i]>0){
      arr[i]="big";
    }
  }
  return arr;
}
console.log(makeItBig([-1,3,5,-5]));

//2.Print Low, Return High - Create a function that takes in an array of 
//numbers.  The function should print the lowest value in the array, and 
//return the highest value in the array.
function lowHigh(arr){
  var arrLength=arr.length;
  var low = arr[0];
  var high = arr[0];

  for (var i = 0;i<arrLength;i++){
    if(arr[i]>high){
      high = arr[i];
    }
    if(arr[i]<low){
      low = arr[i];
    }
  }
  console.log(low);
  return high;
}
var high = lowHigh([1,2,3,4,5,-6]);
console.log(high);

//3.Print One, Return Another - Build a function that takes in an array 
//of numbers.  The function should print the second-to-last value in 
//the array, and return the first odd value in the array.
function oneAnother(arr){
  var arrLength = arr.length;
  console.log(arr[arrLength-2]);
  for (var i=0;i<arrLength;i++){
    if(arr[i]%2==1){
      return arr[i];
    }
  }
  return "no odd values";
}
var odd = oneAnother([1,2,3,4,5]);
console.log(odd);

//4.Double Vision - Given an array (similar to saying 'takes in an array'),
// create a function that returns a new array where each value in the
// original array has been doubled.  Calling double([1,2,3]) should 
//return [2,4,6] without changing the original array.
function doubleVision(arr){
  var arrLength=arr.length;
  arr2=[];
  for (var i=0;i<arrLength;i++){
    arr2[i]=arr[i]*2;
  }
  return arr2;
}
var arr2=doubleVision([1,2,3]);
console.log(arr2);

//5.Count Positives - Given an array of numbers, create a function to 
//replace the last value with the number of positive values found in the 
//array.  Example, countPositives([-1,1,1,1]) changes the original array 
//to [-1,1,1,3] and returns it.
function countPositives(arr){
  var arrLength=arr.length;
  var count=0;
  for(var i=0;i<arrLength;i++){
    if(arr[i]>0){
      count++;
    }
  }
  arr[arrLength-1]=count;
  return arr;
}
console.log(countPositives([-1,1,1,1]));

//6.Evens and Odds - Create a function that accepts an array.  Every 
//time that array has three odd values in a row, print "That's odd!".  
//Every time the array has three evens in a row, print "Even more so!".
function evenOdds(arr){
  var arrLength=arr.length;
  var countOdd=0;
  var countEven=0;
  for(var i=0;i<arrLength;i++){
    if(arr[i]%2==0){
      countEven++;
      if(countEven>2){
        console.log("Even more so!");
        countEven=0;
      }
    }
    
    if(arr[i]%2==1){
      countOdd++;
      if(countOdd>2){
        console.log("That's odd!");
        countOdd=0;
      }
    }
  }
}
evenOdds([1,1,1,2,2,2,3,3,3,44,44,44,44,44,44]);
//7.Increment the Seconds - Given an array of numbers arr, add 1 to every 
//other element, specifically those whose index is odd (arr[1], arr[3], 
//arr[5], etc).  Afterward, console.log each array value and return arr.
function incrementSecs(arr){
  var arrLength=arr.length;
  for(var i=1;i<arrLength;i+=2){
    arr[i]=arr[i]+1;
  }
  console.log(arr);
  return(arr);
}
incrementSecs([1,2,3,4,5,6,7,8,9,10]);
//8,Previous Lengths - You are passed an array (similar to saying 'takes 
//in an array' or 'given an array') containing strings.  Working within 
//that same array, replace each string with a number - the length of the 
//string at the previous array index - and return the array.  For example, 
//previousLengths(["hello", "dojo", "awesome"]) should return 
//["hello", 5, 4]. Hint: Can for loops only go forward?
function previousLengths(arr){
  var arrLength=arr.length;
  for(var i=arrLength-1;i>0;i--){
    arr[i]=arr[i-1].length;  
  }
  return arr;
}
var lengths =previousLengths(["hello","dojo","awesome"]);
console.log(lengths);

//9.Add Seven - Build a function that accepts an array. Return a new 
//array with all the values of the original, but add 7 to each. Do not 
//alter the original array.  Example, addSeven([1,2,3]) should return 
//[8,9,10] in a new array.
function addSeven(arr){
  var arrLength=arr.length;
  arr2=[];
  for (var i=0;i<arrLength;i++){
    arr2[i]=arr[i]+7;
  }
  return arr2;
}
var arr2=addSeven([1,2,3]);
console.log(arr2);

//10.Reverse Array - Given an array, write a function that reverses its 
//values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array,
// but now contains values reversed like so... [2,4,6,1,3].  Do this 
//without creating an empty temporary array.  (Hint: you'll need to swap 
//values).
function reverse(arr){
  var arrLength=arr.length;
  var hold=0;
  for (var i=0;i<arrLength/2;i++){
    hold = arr[i];
    arr[i]=arr[arrLength-1-i];
    arr[arrLength-1-i]=hold;
  }
  return arr;
}
reversearr = reverse([3,1,6,4,2]);
console.log(reversearr);

//11.Outlook: Negative - Given an array, create and return a new one 
//containing all the values of the original array, but make them all 
//negative (not simply multiplied by -1). Given [1,-3,5], return
// [-1,-3,-5].

//12.Always Hungry - Create a function that accepts an array, and prints 
//"yummy" each time one of the values is equal to "food".  If no array 
//values are "food", then print "I'm hungry" once.

//13.Swap Toward the Center - Given an array, swap the first and last 
//values, third and third-to-last values, etc.  Example: 
//swapTowardCenter([true,42,"Ada",2,"pizza"]) turns the array into 
//["pizza", 42, "Ada", 2, true].  swapTowardCenter([1,2,3,4,5,6]) turns 
//the array into [6,2,4,3,5,1].  No need to return the array this time.

//14.Scale the Array - Given an array arr and a number num, multiply all 
//values in the array arr by the number num, and return the changed array 
//arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9].