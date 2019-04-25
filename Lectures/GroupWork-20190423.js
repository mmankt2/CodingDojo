function rotateArr(arr,shiftBy){
  var arrLength = arr.length;
  
  //make shiftBy a positive number
  if (shiftBy <0){
    shiftBy = arrLength+shiftBy;
  }
  
  //set temp arrays to hold the first part and second part of arr
  var arr1 = [];
  var arr2 = [];
  
  //use for loops to save the first and second part of the array
  for (var i = 0;i<arrLength-shiftBy;i++){
    arr1[i]=arr[i];
  }
  for (var k=0;k<shiftBy;k++){
    arr2[k]=arr[arr1.length+k];
  }
  
  //make the new array, shifted
  var newarr = [];
  for (var i = 0;i<arr2.length;i++){
    newarr.push(arr2[i]);
  }
  for (var i = 0; i<arr1.length;i++){
    newarr.push(arr1[i]);
  }
  console.log(newarr);
}
rotateArr([1,2,3,4,5,1,-1],-3);

//now in place
function rotateArr(arr,shiftBy){
  var arrLength = arr.length;
  
  //make shiftBy a positive number
  if (shiftBy <0){
    shiftBy = arrLength+shiftBy;
  }
  
  var hold = 0;//use hold to grab the last value of the array, so it can be placed in front later
  
  //main for loop with tells how many times to shift to the right
  for (var i=0;i<shiftBy;i++){
    hold = arr[arrLength-1]; //use hold to grab the last value of the array, so it can be placed in front later
    
    //use a nested for loop to move each value to the right by one position
    for (var j=arrLength-1;j>0;j--){
      arr[j]=arr[j-1];
    }
    arr[0]=hold;//set the first value to the hold value, which was the last value in the array
  }
  console.log(arr);
}
rotateArr([1,2,3,4,5,1,-1],4);

