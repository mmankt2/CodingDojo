//remove negatives
function removeNegatives(arr){
  var len = arr.length;
  counter = 0;
  for (var i=0; i< len; i++){
    if (arr[i]<0){
      for (var j = i; j<len-counter; j++){
        arr[j] = arr[j+1];
      }
      arr.pop();
      counter++;
    }
  }
  return arr;
}
console.log(removeNegatives([-1,2,3,-1,2,3,4,5,-2]))

//second to last
function secondToLast(arr){
  if (arr.length < 2){
    return null;
  }
  return arr[arr.length-2];
}
console.log(secondToLast([3]))

//second largest
function secondLargest(arr){
  if (arr.length < 2){
    return null;
  }
  var len = arr.length;
  var max = arr[0];
  for (var i = 0; i< len; i++){
    if (arr[i] > max){
      max = arr[i];
    }
  }
  secondHighest = arr[0];
  if (secondHighest = max){
    secondHighest = arr[1];
  }
  for (var i = 0; i< len; i++){
    if (arr[i]>secondHighest && arr[i] < max){
      secondHighest = arr[i];
    }
  }
  return secondHighest;
}
console.log(secondLargest([3,2,1,2,3,4,5,6]))

//nth to last
function nthToLast(arr,n){
  if (arr.length < n){
    return null;
  }
  return arr[arr.length-n];
}
console.log(nthToLast([1,2,3,4],2))

//nth largest
function nthLargest(arr,n){
  var len = arr.length;
  counter = 0;
  if (len < n){
    return null;
  }
  for (var i = 0; i < len; i++){
    counter = 0;
    for (var j = 0; j < len; j++){
      if (arr[j] > arr[i]){
        counter++;
      }
    }
    if (counter == n - 1){
      return arr[i];
    }
  }
  return null;
}
console.log(nthLargest([1,2,3,4,5,6,-3,-2],3))