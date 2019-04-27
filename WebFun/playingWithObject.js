var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

console.log(users[1].age);//30
console.log(users[0].name); //Michael
var i = 0;
while (i< users.length){
  console.log(users[i].name + " = " + users[i].age);
  i++;
}