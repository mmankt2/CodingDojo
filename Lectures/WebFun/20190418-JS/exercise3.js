// Oddities
// Build a function that takes in 3 arguments: 2 numbers and a string.
// If the sum of the numbers is odd, print the string.
// If the sum of the numbers is even, print "None Shall Pass"
// If the numbers are the same, print "Quite the Pair"
// If both numbers are negative, print "Somebody Needs a Pep Talk!"

function oddities(num1,num2,str){
  var sum = num1 + num2;
  if (sum % 2 ==1){
    console.log(str);
  }
  else {
    console.log("None Shall Pass");
  }

  if(num1==num2){
    console.log("Quite the Pair");
  }

  if(num1<0 && num2<0){
    console.log("Somebody Needs a Pep Talk");
  }

}

oddities(5,6,"none");