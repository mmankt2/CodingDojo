//push front
function push_front(arr,x){
  len = arr.length;
  for (var i = len; i>0; i--){
    arr[i] = arr[i-1]
  }
  arr[0] = x;
  return arr;
}
console.log(push_front([1,2,3],0))

//pop front
function pop_front(arr){
  len = arr.length;
  front = arr[0];
  for (var i = 0;i<len - 1;i++){
    arr[i] = arr[i+1];
  }
  arr.pop();
  return_values = [front,arr]
  return return_values;
}
console.log(pop_front([1,2,3]))

//insert at
function insert_at(arr,i,x){
  len = arr.length;
  for (var j = len; j > i; j--){
    arr[j] = arr[j-1];
  }
  arr[i] = x;
  return arr;
}
console.log(insert_at([1,2,3],1,2))

//remove at
function remove_at(arr,i){
  len = arr.length;
  value_at_i = arr[i];
  for (var j = i; j<len -1; j++){
    arr[j] = arr[j+1];
  }
  arr.pop();
  return_values = [value_at_i,arr];
  return return_values;
}
console.log(remove_at([1,2,3],1))

//swap pairs
function swap_pairs(arr){
  len = arr.length;
  if (len % 2 == 0){ 
    end = len;
  }
  else {
    end = len-1;
  }
  for (var i = 0; i < end; i+=2){
    hold = arr[i];
    arr[i] = arr[i+1];
    arr[i+1] = hold;
  }
  return arr;
}
console.log(swap_pairs([1,2,3,4]))

//remove duplicates
function remove_dups(arr){
  len = arr.length;
  newarr=[];
  for (var i = 0; i < len; i++){
    if(arr[i] != arr[i+1]){
      newarr.push(arr[i]);
    }
  }
  arr = newarr;
  return arr;
}
console.log(remove_dups([1,1,1,2,2,3,3,3,3]))