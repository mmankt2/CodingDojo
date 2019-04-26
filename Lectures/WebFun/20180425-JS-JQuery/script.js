//the DOM document object model
var obj = {
  name:"Melissa",
  //a function inside an object is called a "method"
  ability: function sayHello(){
    console.log("Hello");
  }//
}

console.dir(document);//allows us to mess with the HTMLs objects.

document.title="New Title";
document.getElementsByTagName("h1");

console.dir(document.getElementsByTagName("h1")[0]);

document.getElementsByTagName("h1")[0].innerText = "Awesome";

//affect all h1 tags with jquery
$("h1").text("jQuery Rulez");

//affect just the h1 tag with id second
$("#second").text("This is cool");

//run a function called a "call back" when a thing is clicked
//affects all h1s when you click
$("h1").click(function(){
  $("h1").css("background-image","linear-gradient(purple,red,blue,yellow,orange,green)");
})

//affects whichever h1 you click.
$("h1").click(function(){
  $(this).css("background-image","linear-gradient(purple,red,blue,yellow,orange,green)");
})