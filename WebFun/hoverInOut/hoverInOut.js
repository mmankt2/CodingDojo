$(document).ready(function(){
var page = [
  [1,1,1,1],
  [2,2,2,2]
];

console.log('workng in jquery');
var contents =''
for (var i = 0; i<page.length;i++){
  contents+='<div id="row">';
  for (var j=0; j<page[i].length;j++){
    contents+='<img src="cat'+ j + '.png" atl="cat' + j + '">';
  }
  contents+='</div>';
}

$('#container').after(contents);

$('img').hover(function(){
  var imgattr=$(this).attr('src');
  imgattr=imgattr.replace(/cat/g,'ninja');
  $(this).attr('src',imgattr);
}, function(){
    var imgattr=$(this).attr('src');
    imgattr=imgattr.replace(/ninja/g,'cat');
    $(this).attr('src',imgattr);
  }
);

console.log(contents);

})//end of document.ready