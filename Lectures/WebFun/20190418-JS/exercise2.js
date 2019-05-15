// challenge 1 - Fix this code so that we avoid the previous error.
function thisLengthThatNumber(num1, num2){
    var newArr = [];
    //newArr.length = num1;
    for (var i = 0; i <= num1; i++){
        newArr[i] = num2;
    }
    return newArr;
}
console.log(thisLengthThatNumber(3,4)); // expect: [4,4,4]
console.log(thisLengthThatNumber(2,2)); // expect: [2,2]

// challenge 2 - Fix the code so that the given array has each
// of its values shifted one position to the right and return it. 
// Example: given [1,2,3] return [1,1,2,3]
function shiftRight(arr){

    for (var i = arr.length; i > 0; i--){
        arr[i] = arr[i-1];
    }
    return arr;
}

console.log(shiftRight([1,2,3]));