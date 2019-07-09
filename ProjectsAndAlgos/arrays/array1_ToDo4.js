//shuffle
function shuffle(arr){
  var len = arr.length;
  for (var i = 0; i < len; i++){
    randomIndex = Math.floor(Math.random()*len)
    hold = arr[randomIndex];
    arr[randomIndex] = arr[i];
    arr[i] = hold;
  }
  return arr;
}
console.log(shuffle([1,2,3,4,5]))

//remove range
function removeRange(arr,start,end){
  var len = arr.length;
  range = end - start +1;
  if (start > end){
    return null;
  }
  if (end > len){
    return null;
  }
  for (var i = start; i < len; i++){
    arr[start] = arr[start + range];
  }
  for (var i = 0; i < range; i++){
    arr.pop();
  }
  return arr;
}
console.log(removeRange([2,3,4,5,6,7],2,4))

//intermediate sums
function intermediateSums(arr){
  var len = arr.length;
  console.log(len);
  var new_len = len;
  var new_arr = [];
  var counter = 0;
  var sum = 0;
  //figure out how long the returned array has to be, add 1 for every 10 numbers
  if (len % 10 == 0){
    new_len = Math.floor(len/10) + len;
    console.log(new_len);
  }
  else {
    new_len = Math.floor(len/10) + len + 1;
    console.log(new_len);
  }

  for (var i = 0; i < new_len; i++){
    if (i % 10 == 0 && i !=0 ){
      new_arr[i] = sum;
      counter++;
      sum = 0;
      continue;
    }
    new_arr[i] = arr[i-counter];
    if ( i == new_len - 1){
      new_arr[i] = sum;
    }
    sum = sum + arr[i-counter];
  }
  console.log(new_arr.length)
  return new_arr;
}
console.log(intermediateSums([1,2,1,2,1,2,1,2,1,2]))

//double trouble
function doubleTrouble(arr){
  var len = arr.length;
  //start at the end and work my way to the front of the array
  for (var i = len * 2 - 1; i >= 0; i--){
    if (i % 2 == 0){
      arr[i] = arr[i/2];
    }
    else {
      arr[i] = arr[(i-1)/2]
    }
  }
  return arr;
}
console.log(doubleTrouble([4,"Ulysses",42,false]))

//zip it
function zipIt(arr1, arr2){
  var len1 = arr1.length;
  var len2 = arr2.length;
  var new_len = len1 + len2;
  if (len1 <= len2) {
    for (var i = len1 * 2 - 1; i >= 0; i--){
      if (i % 2 == 0){
        arr1[i] = arr1[i/2];
      }
    }
    var i = new_len-1;
    while (i > 0){
      if (i >= len1*2 - 1){
        arr1[i] = arr2[i - len1];
      }
      if (i % 2 != 0 && i < len1*2 - 1){
        arr1[i] = arr2[(i+1)/2 -1]
      }
      i--;
    }
  }
  if (len1 > len2){
    for (var i = new_len - 1; i >= len2*2; i--){
      arr1[i] = arr1[i - len2]
    }
    for (var i = len2*2 - 1; i >= 0; i--){
      if (i % 2 == 0){
        arr1[i] = arr1[i/2]
      }
      else {
        arr1[i] = arr2[(i+1)/2 - 1]
      }
    }
  }
  return arr1;
}
console.log(zipIt([1,2,3,4,5],[10,30]))