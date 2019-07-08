var funStr = "Emma shreds on her electric cello";
console.log(typeof funStr); //"string"
var oneChar = funStr[26]; // "c"
console.log(typeof oneChar); //"string"

//string.length
console.log(funStr.length); //33
console.log("".length);//0

//string.split
wordArray = funStr.split(" ");
//["Emma","shreds","on","her","electric","cello"]
console.log(wordArray [5].split(""));
//["c","e","l","l","o"]

//array.join converts array to string
console.log(wordArray.join());
//a comma is used by default: "Emma,shreds,on,her,electric,cello"
console.log(wordArray.join("-"));
//"Emma-shreds-on-her-electric-cello"


//switch/case statements
switch (favoriteLanguageString) {
  case 'JavaScript': console.log("Ah so, we thrive on chaos!"); break;
  case 'Python': console.log("Parenthesis-haters, unite!"); break;
  case 'PL/I': console.log("Wha? Who let you in here?");
  default: console.log("Why don't you choose a different one.");
  }
  
//integer to roman numerals

var myAssocArr = { fName: "Kaitemma", "lName": "Claiben"};
// notice that keys can be strings (quoted) or symbols (without quotes)
myAssocArr["fun"] = "shreds on electric cello";
console.log(myAssocArr); 
// { fName: "Kaitlemma", lName: "Claiben",
// fun: "shreds on her electric cello" }
myAssocArr.IQ = 144;
console.log(myAssoc["IQ"]); // 144
console.log(myAssoc.fun); // "shreds on her electric cello"
