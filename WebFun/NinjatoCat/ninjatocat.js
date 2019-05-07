$(document).ready(function(){

console.log('working in js');
$('img').click(function(){
  //console.log('clicked image');
  //console.log($(this).attr('alt-src'));
 $(this).attr('src',$(this).attr('alt-src')); 
});

})//end of document.ready