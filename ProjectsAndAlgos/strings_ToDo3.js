//parens valid
function parensValid(str){
  splitStr = str.split("");
  splitStrLen = splitStr.length;
  countOpen = 0;
  countClose = 0;
  for (var i = 0; i < splitStrLen; i++){
    if (splitStr[i] == '('){
      countOpen++;
    }
    if (splitStr[i] == ')'){
      countClose++;
    }
    if (countClose > countOpen){
      return false;
    }
    if ( i == splitStrLen -1 && countOpen != countClose){
      return false;
    }
  }
  return true;
}
console.log(parensValid('Y(2)d)'))

//braces valid = try 1
//can't get it to work with this kind of sequence '(awke{'sl)k}'
function bracesValid(str){
  splitStr = str.split("");
  splitStrLen = splitStr.length;
  countOpenParen = 0;
  countCloseParen = 0;
  countOpenBrack = 0;
  countCloseBrack = 0;
  countOpenBrace = 0;
  countCloseBrace = 0;
  for (var i = 0; i < splitStrLen; i++){
    //return false right away if the count of the closers is bigger than openers
    if (countCloseParen > countOpenParen || countCloseBrack > countOpenBrack || countCloseBrace > countOpenBrace){
      return false;
    }
    switch (splitStr[i]){
      case '(': countOpenParen++; break;
      case '{': countOpenBrace++; break;
      case '[': countOpenBrack++; break;
    }
    switch (splitStr[i]){
      case ')': countCloseParen++; break;
      case '}': countCloseBrace++; break;
      case ']': countCloseBrack++; break;
    }
    //these next 3 if statements were added to try and count situations like these where it shoudl return false '(awke{'sl)k}'
    //but it doesn't work. 
    if (countCloseParen == countOpenParen){
      countCloseParen = 0;
      countOpenParen = 0;
      if (countOpenBrace != countCloseBrace || countOpenBrack != countCloseBrack){
        return false;
      }
    }
    if (countCloseBrack == countOpenBrack){
      countCloseBrack = 0;
      countOpenBrack = 0;
      if (countOpenBrace != countCloseBrace || countOpenParen != countCloseParen){
        return false;
      }
    }
    if (countCloseBrace == countOpenBrace){
      countCloseBrace = 0;
      countOpenBrace = 0;
      if (countOpenParen != countCloseParen || countOpenBrack != countCloseBrack){
        return false;
      }
    }
    //at the end, make sure the count of openers equals count of closers
    if ( i == splitStrLen -1 && (countOpenParen != countCloseParen || countOpenBrace != countCloseBrace || countOpenBrack != countCloseBrack )){
      return false;
    }
  }
  return true;
}
console.log(bracesValid('W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!'))


//braces valid - try 2
//still can't get it to work with this kind of sequence '(awke{'sl)k}'
function bracesValid(str){
  var splitStr = str.split("");
  var splitStrLen = splitStr.length;
  
  var openingBraces = ['(','{','['];
  var closingBraces = [')','}',']'];
  var bracePairs = {
    ')':'(',
    '}':'{',
    ']':'['
  };
  var lastOpener = [];
  
  for (var i = 0; i < splitStrLen; i++){
    if (openingBraces.includes(splitStr[i])){
      lastOpener = splitStr[i];
    }
    if (closingBraces.includes(splitStr[i])){
      var lastClosingMatch = lastOpener.pop();
      if (lastClosingMatch != bracePairs[splitStr[i]]){
        return false;
      }
    }
    return lastOpener.length == 0; //return true if there's no last opener
  }
}
console.log(bracesValid('A(1)s[O (n]0{t) 0}k'))

//is palindrome
function isPalindrom(str){
  strSplit = str.split("");
  strSplitLen = strSplit.length;
  loopLen = Math.floor(strSplitLen/2)

  for (var i = 0; i <= loopLen; i++){
    if (strSplit[i] != strSplit[strSplitLen - 1 - i]){
      return false;
    }
  }
  return true;
}
console.log(isPalindrom('a x a'))

//longest Palindrome
function longPalindrome(str){
  var strSplit = str.split("");
  var strSplitLen = strSplit.length;
  console.log(strSplitLen);
  var longestPalWord = "";
  var currentPal = [];
  var currentPalWord = "";
  //make a loop that starts with the letter, then checks before and after to see if they match. 
  //if they match then save it as the longest palindrome. If they don't match then move on to the next letter.
  for (var i = 0; i < strSplitLen; i++){
    //console.log("i ="+i);
    for (var j = 1; j <= Math.floor(strSplitLen/2); j++){
      //console.log("j ="+j);
      if (currentPalWord.length > longestPalWord.length){
        longestPalWord = currentPalWord;
        console.log('longest pal is '+longestPalWord)
      }
      if (strSplit[i-j] == strSplit[i+j]){
        //console.log(strSplit[i-j],strSplit[i],strSplit[i+j]);
        currentPal[i-j] = strSplit[i-j];
        currentPal[i] = strSplit[i];
        currentPal[i+j] = strSplit[i+j];
        //currentPalWord = currentPal.split("");
        currentPalWord = currentPal.join("");
        console.log('currentPalWord is '+currentPalWord);
        currentPalLength = currentPal.length;
      }
      if (strSplit[i-j] != strSplit[i+j]){
        currentPal = [];
        break;
      }
    }
  }
  return longestPalWord;
}
console.log(longPalindrome('Hot puree eruption!'));