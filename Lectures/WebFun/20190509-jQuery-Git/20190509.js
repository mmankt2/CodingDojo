$(document).ready(function(){

console.log('working in jquery');

$('h1').on("click",function(){
  $(this).append("<p>new paragraph</p>");
});

});//end of document.ready