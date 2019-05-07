$(document).ready(function(){

  $('img').click(function(){
  var imgattr = $(this).attr('src');
  
  if (/cat/.test(imgattr)){
    imgattr=imgattr.replace(/cat/g,'ninja');
  }
  else {
    imgattr=imgattr.replace(/ninja/g,'cat');  
  }

  $(this).attr('src',imgattr);
});

})//end of document.ready