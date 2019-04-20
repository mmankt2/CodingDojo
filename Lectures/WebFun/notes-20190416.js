var num = 5.5; //numbers 5 or 5.5 or 5e10
var name = "Giovanni"; // strings
var arr = [5,"Gio",5.5,[0,1]];

console.log(arr[1]);//"Gio"
console.log(arr.length);//4 . gives the length of arr
arr[1]="Richard";//[5,"Richard",5.5,[0,1]]
arr[1]=arr[2];//arr[1]=5.5, [5,5.5,5.5.[0,1]]
arr[2]=arr[2]+1;//[5,5.5,6.5,[0,1]]


var gio = {
  numDogs: 5,
  name: "Gio",
  height: 5.5,
  favoriteNumbers:[0,1],
  sayHi: function(){ console.log("Hello World")}
}

console.log(gio.numDogs);//5
gio.numDogs = -1;
console.log(gio.numDogs);//-1

//example of how the console object was made below
var console = {
  log:function(){}
}

console.log(gio.sayHi());//"Hello World"