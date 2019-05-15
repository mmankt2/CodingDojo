function printnums(){
  var a = 1;
  while (a<=255){
    console.log(a);
    a++;
  }  
}
printnums();

function printevens(){
  var a=2;
  while(a<=255){
    console.log(a);
    a=a+2;
  }
}
printevens();

function printarr(arr){
  for(var i = 0; i<arr.length;i++){
    console.log(arr[i]);
  }
}
printarr([1,2,3]);

function lucky(arr){
  for(var i=0;i<arr.length;i++){
    if(arr[i]%7==0){
      arr[i]="Lucky";
    }
  }
  return arr;
}
var newarr = lucky([1,7,6,14]);
console.log(newarr);

function insertAt(arr,index,value){
  var arrLength = arr.length;//4
  for (var i=arrLength;i>=index;i--){
    arr[i]=arr[i-1];
  }
  arr[index]=value;
  return arr;
}
var newarr = insertAt([1,2,3,4,5,6,7,8,9],3,8);
console.log(newarr);