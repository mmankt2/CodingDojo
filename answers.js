//page 4
//1. two
//2. == data types can be different. === data types
//   must be the same
//3. boolean (true/false)

//Review the first 22 pages of the Algorithm Book and complete
//all assignments on page 16, 20, and 22.
//Type your answers in a single file called answers.js
//or answers.txt and upload the code the learn.codingdojo.com

//Date: 2019 March 31

//Author: Melissa Littleton

//page 5
console.log("Hello World");
var message = "Welcome to the dojo";
console.log(message);

//page 6
function sayMyName()
{
    console.log("My name is Melissa");
}

sayMyName();

//page 7
if (myName == "Melissa")//expression is evaluated
{
    //this code runs if the expression evaluates to TRUE
    console.log("Her there Melissa, how's it going?");
}
else
{
    //this code runs if the expression evaluates to FALSE
    console.log("Greetings human being. Have a great day!");
}

//page 8
if (today == "Friday" && moodLevel >=100)//example of AND operator
{
    goDancing();
}
if (raining==true||distanceMiles > 3)//example of OR operator
{
    callUber();
}
if (!snowing)//example of NOT operator
{
    bravelyDonSomeShorts();
}

//page 9 - chaining if statements
if (myName == "Melissa")
{
    console.log("Hey Melissa, how's it going?");
}
else if (myName=="Paul")
{
    console.log("Hey Paul, what schoolwork do you have today?");
}
else
{
    console.log("Greetings human. Have a great day!");
}

//page 10 - Loops
//For loops good for a loop that runs XX times
//while loops good for a loop that runs until a specific condition met

//for (INITIALIZATION; Test; Increment/Decreemnt)
for (var num = 1; num < 6; num = num +1)
{
    console.log("I'm counting! The number is ", num);
}
console.log("We are done. Goodbye world!");

//while loop
var num = 1;
while (num < 6)
{
    console.log("I'm counting! The number is "+ num);
    num = num +1;
}
console.log("We are done. Goodbye world!");

//page 13 - break and continue
//BREAK: exits the entire loop immediately
//CONTINUE: exits the current curly brackets but continues in the loops

//page 14 - functions and parameters
function greetSomeone(person)
{
    if (person=="Melissa"){
        console.log("hey Melissa, hows it going?");
    }
    else{
        console.log("greetings human");
    }
}

//Homework: page 16

//setting and swapping
var myNumber = 42;
var myName = "Melissa";
var hold = myName; //create a hold variable
myName = myNumber; //swap myName to be myNumber
myNumber = hold; //swap myNumber to be myName

//print -52 to 1066;
for (var i = -52;i < 1067; i++){
    console.log(i);
}

//don't worry, be happy
function beCheerful(){
    console.log("good morning!")
}
var i = 1;
while (i < 99){
    beCheerful();
    i++;
}

//multiples of three - but not all
for (var multiple = -300; multiple <=0; multiple +=3)
{
    if(multiple == -3 || multiple == -6)
    {
        continue;
    }
    console.log(multiple);
}

//printing integers with while
var i = 2000;
while (i <= 5280){
    console.log(i);
    i++;
}

//you say it's your birthday
var today=3103;
if(today == 2809){
    console.log("How did you know?");
}
else {
    console.log("Just another day....");
}

//leap year
var year = 2019;
if (year % 400 === 0){
    console.log("it's a leap year")
}
else if (year % 4 === 0 && year % 100 !=0){
    console.log("it's a leap year")
}
else{
    console.log("it's not a leap year")
}

//print and count
var i = 512;
var count = 0;//variable to store the count
while (i <=4096){
    if (i % 5 === 0){
        console.log(i);
        count++;
    }
    i++;
}
console.log(count);

//multiples of six
var i = 0;
while(i<=60000){
    if(i % 6 === 0){
        console.log(i);
    }
    i++;
}

//counting, the dojo way
for(var i = 1; i <=100;i++){
    if(i % 5 === 0 && i % 10 != 0){
        console.log("Coding");
    }
    else if (i % 10 === 0){
        console.log("Dojo");
    }
    else{
        console.log(i);
    }
}

//What do you know?
var myparam = "this is my parameter"
function myFunc(incoming){
    console.log(incoming);
}
myFunc(myparam);

//Whoa, that sucker's huge...
var i = -300000;
var sum = 0;
while (i<=300000){
    if(i % 2 === 0){
        sum = sum + i;
    }
    i++;
}
console.log(sum);

//Countdown by Fours
var i = 2016;
while ( i > 0){
    console.log(i);
    i = i-4;
}

//flexible countdown
var lowNum = 0;
var highNum = 20;
var mult = 3;
while (highNum >= lowNum){
    console.log(highNum);
    highNum = highNum - 3;
}

//Final countdown
var param1 = 10;
var param2 = 0;
var param3 = 100;
var param4 = 40;

while(param2 <=param3){
    if (param2 == param4){
        continue;
    }
    console.log(param2);
    param2 = param2 + param1;
}

//page 20. Chapter 1 - Fundamentals
//Countdown
var mynum = 10;
function countdown(inputnum){
    var newarr = [inputnum];
    inputnum--;
    while (inputnum >=0){
        newarr.push(inputnum);
        inputnum--;
    }
    return newarr;
}
var myarr = countdown(mynum);
console.log(myarr);

//print and return
var myarr = [1,2];
function printarr(arr){
    console.log(arr[0]);
    return arr[1];
}
var myval = printarr(myarr);
console.log(myval);

//first plus length
var myarr = [1,2,3,4];
function arrayfunc(arr){
    var sum = arr[0]+arr.length;
    return sum;
}
var myval = arrayfunc(myarr);
console.log(myval);
//if the first value in the array is a string, then the
//sum gets converted to a string.
//if the first value is a boolean, then false is treated
//as 0 and true is treated as 1, and sum is still a number.

//values greater than second
var myarr = [1,3,5,7,9,13];
function printvals(arr){
    var len = arr.length;
    var sum = 0;
    for (var i = 0; i < len; i++){
        if (arr[i] > arr[1]){
            console.log(arr[i]);
            sum = sum + 1;
        }
    }
    return sum;
}
var mysum = printvals(myarr);
console.log(mysum);

//values greater than second, generalized
var myarr = [1,3,5,7,9,13];
function printvals(arr){
    var len = arr.length;
    //check if the array is only 1 element long
    if (len <= 1){
        return;
    }
    var sum = 0;
    for (var i = 0; i < len; i++){
        if (arr[i] > arr[1]){
            console.log(arr[i]);
            sum = sum + 1;
        }
    }
    return sum;
}
var mysum = printvals(myarr);
console.log(mysum);

//this length, that value
var mynum1 = 2;
var mynum2 = 1;
function jinx(num1,num2){
    var i = 0;
    var arr = [];
    while (i < num1){
        arr.push(num2);
        i++;
    }
    return arr;
}
var myarr = jinx(mynum1,mynum2);
console.log(myarr);

//fit the first value
var myarr=[5,1,2,3];
function arrlen(arr){
    if (arr[0]>arr.length){
        console.log("Too big!");
    }
    else if (arr[0]<arr.length){
        console.log("Too small!");
    }
    else{
        console.log("Just right!");
    }
}
arrlen(myarr);

//fahrenheit to celsius
function fahrenheitToCelsius(fDegrees){
    var cDegrees = (fDegrees - 32)*5/9;
    return cDegrees;
}
var farhenheit = 212;
var celsius = fahrenheitToCelsius(farhenheit);
console.log(celsius);

//celsius to fahrenheit
function celsiusToFahrenheit(cDegrees){
    var fDegrees = (9/5*cDegrees)+32;
    return fDegrees;
}
var celsius = 0;
var fahrenheit = celsiusToFahrenheit(celsius);
console.log(fahrenheit);


//page 22. Chapter 1 - Fundamentals
//biggie size
var myarr = [-1,3,5,-5];
function biggiesize(arr){
    var len = arr.length;
    for (var i = 0; i < len; i++){
        if (arr[i]>0){
            arr[i]="big";
        }
    }
    return arr;
}
var mynewarr = biggiesize(myarr);
console.log(mynewarr);

//print low, return high
var myarr = [-1,3,5,-5];
function lowHigh(arr){
    var len = arr.length;
    var min = arr[0];
    var max = arr[0];
    for (var i = 1; i < len; i++){
        if (arr[i]<min){
            min = arr[i];
        }
        else if (arr[i]>max){
            max = arr[i];
        }        
    }
    console.log(min);
    return max;
}

var maxval = lowHigh(myarr);
console.log(maxval);

//print one, return another
var myarr = [-1,3,5,-5];
function oneAnother(arr){
    var len = arr.length;
    console.log(arr[len-1]);//print second to last value
    var i = 0;
    while (i <= len){
        if (arr[i] % 2 != 0){
            return arr[i];
        }
        i++;
    }
    return;
}
var oddval = oneAnother(myarr);
console.log(oddval);

//double vision
var myarr = [-1,3,5,-5];
function doubleVision(arr){
    var len = arr.length;
    var newarr = [];
    var i = 0;
    while (i<len){
        newarr.push(2*arr[i]);
        i++;
    }
    return newarr;
}
var mydoublearr = doubleVision(myarr);
console.log(mydoublearr);

//count positives
var myarr = [-1,3,5,-5];
function countPositives(arr){
    var len = arr.length;
    var i = 0;
    var sum = 0;
    while (i<len){
        if(arr[i]>0){
            sum++;
        }
        i++;
    }
    arr[len-1]=sum;
    return arr;
}
var mynewarr = countPositives(myarr);
console.log(mynewarr);

//evens and odds//this still needs some more
var myarr = [-1,-2,-3,1,3,5,-1,-2,-5,2,2];
function evensOdds(arr){
    var len = arr.length;
    var i = 3;
    var counter = 3;
    while (i<len){
        if (arr[i-counter] % 2 != 0){
            counter = counter -1;
            if (counter == 0){
                console.log("That's odd!");
                counter = 3;
            }
        }
        else if (arr[i-counter] % 2 === 0){
            counter = counter -1;
            if (counter ==0){
                console.log("Even more so!");
                counter = 3;
            }
        }
        i++;
    }
}
evensOdds(myarr);

//increment the seconds
var myarr =  [-1,-2,-3,1,3,5,-1,-2,-5,2,2];
function increment(arr){
    var len = arr.length;
    var i = 0;
    while (i<len){
        if(arr[i] % 2 != 0){
            arr[i] = arr[i]+1;
        }
        i++;
    }
    return arr;
}
var mynewarr = increment(myarr);
console.log(mynewarr);

//previous lengths
