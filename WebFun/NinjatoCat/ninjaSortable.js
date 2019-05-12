$(document).ready(function(){
  console.log('in jquery');
$( function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
  })
});