function paintTheHouse(color,brush){
  console.log("Painting the house", color,"with a", brush);
  return brush; //toothbrush
}
var result = paintTheHouse("green","toothbrush");
console.log(result); //toothbrush

//conditionals and modulo
function checkIt(num){
  if (num % 2 == 0 && num % 10 ==0){
    console.log("Even Number");
  } 
  else if (num % 3 == 0){ //else if happens even when if is true
    console.log("Evenly divisible by 3");
  }
  else {
    //this is a catch all if the if and else if is false.
  }
}