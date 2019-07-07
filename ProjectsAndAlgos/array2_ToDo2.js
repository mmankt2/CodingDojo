

//array: binary search
//this function isn't working properly.  
function returnFalse(arr,start,end,x){
  console.log(arr[start]);
  console.log(arr[end]);
  if (x < arr[start]){
    end = Math.floor(end/2);
    start = 0;
    returnFalse(arr,start,end);
  }
  if (x > arr[end]){
    start = Math.floor(end/2);
    end = len;
    returnFalse(arr,start,end);
  }
  if (x == arr[start] || x == arr[end]){
    return true;
  }
}

function binarySearch(arr,x){
  var len = arr.length;
  var i = 0;
  while (i >= 0){
    //first check if x is even in the range of arr
    if (x < arr[0] || x > arr[len -1]){
      return false;
    }
    console.log(Math.floor(len/2));
    if (x > arr[Math.floor(len/2)]){
      var start = Math.floor(len/2) + 1;
      var end = len - 1;
      console.log("in x > section. end="+end+" start="+start)
      returnFalse(arr,start,end,x)
    }
    if (x <= arr[Math.floor(len/2)]){
      var start = 0;
      var end = Math.floor(len/2);
      console.log("in x <= section. end="+end+" start="+start)
      returnFalse(arr,start,end,x);
    }
  }
}
console.log(binarySearch([1,2,3,4,5],3))