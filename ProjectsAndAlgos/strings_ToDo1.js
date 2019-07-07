//Remove Blanks
function removeBlanks(stg){
  stg = stg.split(" ").join("");
  return stg;
}
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));

//get digits
function getDigits(stg){
  var charArray = stg.split("");
  var len = charArray.length;
  console.log(len);
  numArray = [];
  for (var i = 0; i < len; i++){
    //console.log(charArray[i], typeof (charArray[i] +0));
    //console.log(typeof parseInt(charArray[i]));
    if (isNaN(charArray[i])){
      continue;
    }
    else {
      numArray.push(charArray[i]);
    }
  }
  numArray = numArray.join("");
  numArray = parseInt(numArray);
  return numArray;
}
console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"))

//acronyms
function acronym(stg){
  var wordArray = stg.split(" ");
  var wordArrLen = wordArray.length;
  var acro = [];
  for (var i = 0; i<wordArrLen; i++){
    acro.push(wordArray[i][0]);
  }
  acro = acro.join("");
  return acro;
}
console.log(acronym("Live from New York, it's Saturday Night!"))

//count non-spaces
function countNonSpace(stg){
  var len = stg.length;
  var count = 0;
  for (var i = 0; i< len; i++){
    if (stg[i] != " "){
      count++;
    }
  }
  return count;
}
console.log(countNonSpace("Honey pie, you are driving me crazy"))

//remove shorter strings
function removeShortStrings(arr,len){
  var arrLen = arr.length;
  var newArr = [];
  for (var i = 0; i< arrLen; i++){
    if (arr[i].length >= len){
      newArr.push(arr[i]);
    }
  }
  return newArr;
}
console.log(removeShortStrings(['hello','my','name','is','melissa'],5));