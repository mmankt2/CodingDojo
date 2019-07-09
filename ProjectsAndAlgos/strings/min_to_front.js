function minToFront(arr){
  var len = arr.length;
  var min = arr[0];
  for (var i = 0; i<len-1;i++){
    if(arr[i+1]<arr[i]){
      min = arr[i+1];
      minIndex = i+1;
    }
  }
  var hold = arr[0];
  for (var i = minIndex; i>0; i--){
    arr[i] = arr[i-1];
  }
  arr[0] = min;
  return arr;
}
console.log(minToFront([1,1,2,7,4,1,0,-6]))