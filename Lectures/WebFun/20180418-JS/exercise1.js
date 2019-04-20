// challenge 1
function makeDinner(ingredient1, ingredient2, minutes){
   console.log("mixing in:", ingredient1);
   if (ingredient2 == "Hot Sauce"){
       console.log("SPICY");
       if (minutes > 90){
            console.log("slow and low");
       }
   }else{
       console.log("MILD");
   }
}
makeDinner("tomato sauce", "sugar", 60);
makeDinner("salt", "Hot Sauce", 90);
makeDinner("beans", "Hot Sauce", 120);

// challenge 2
function thisLengthThatNumber(num1, num2){
    var newArr = [];
    newArr.length = num1;
    for (var i = 0; i <= newArr.length; i++){
        newArr[i] = num2;
    }
    return newArr;
}
console.log(thisLengthThatNumber(2,4));
console.log(thisLengthThatNumber(2,2)); // explain this outcome