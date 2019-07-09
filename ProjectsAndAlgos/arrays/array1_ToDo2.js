//Reverse
function reverse_array(arr){
  var len = arr.length;
  for (var i = 0; i < len/2; i++){
    hold = arr[i];
    arr[i] = arr[len-1-i];
    arr[len-1-i] = hold;
  }
  return arr;
}
console.log(reverse_array([1,2,3,4,5]));

//Rotate
function rotateArr(arr,shiftBy){
  var len = arr.length;
  for(var i = 0; i < shiftBy; i++){
    arr1 = arr[i];
  }
  for (var i=shiftBy-1; i<len; i++){
    arr2 = arr[i];
  }
  for (var i=0; i<arr2.length; i++){
    arr1.push(arr2[i])
  }
  return arr1;
}
console.log(rotateArr([1,2,3,4,5],2))

//filter ranges
function filterRange(arr,min,max){
  if (min > max){
    return "Min mus be less than max";
  }
  var len = arr.length;
  new_len = max-min+1;
  for (var i = 0; i < new_len; i++){
    arr[i] = arr[min+i];
  }
  popOff = len - new_len;
  for (var i = len -1; i >= new_len; i--){
    arr.pop();
  }
  return arr;
}
console.log(filterRange([1,2,3,4],1,3))

//concat
function my_concat(arr1, arr2){
  var len2 = arr2.length;
  new_arr = arr1;
  for (var i=0; i< len2; i++){
    new_arr.push(arr2[i])
  }
  return new_arr;
}
console.log(my_concat([1,2,3],['a','b']))

//skyline heights
function skyline(arr){
  var len = arr.length;
  new_arr = [];
  for (var i = 0;i<len; i++){
    console.log("in for loop")
    if (i == 0){
      if (arr[i] > 0){
        new_arr.push(arr[i]);
      }
    }
    if (i > 0){
      if (arr[i] > arr[i-1]){
        new_arr.push(arr[i]);
      }
    }
  }
  return new_arr;
}
console.log(skyline([1,-1,2,3,1,5,-3]))