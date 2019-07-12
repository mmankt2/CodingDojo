$(document).ready(function() {
console.log('working in jquery');

$('#fn').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if (this.value.length < 2){
    $('.fn').show();
  }
  if (this.value.length >=2 ){
    $('.fn').hide();
  }
}, 500));

$('#ln').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if (this.value.length < 2){
    $('.ln').show();
  }
  if (this.value.length >=2 ){
    $('.ln').hide();
  }
}, 500));

$('#email').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if( !isValidEmailAddress( this.value ) ) { 
    $('.email').show();
  }
  else{
    $('.email').hide();
  }
}, 500));

$('#password').keyup(delay(function(e){
  //console.log('on keyup function');
  password1 = this.value;
  if( !isValidPW( this.value ) ) { 
    $('.password').show();
    $('#btnSubmit').attr("disabled",true);

    //   disableSubmit();
  }
  else{
    $('.password').hide();
    $('#btnSubmit').attr("disabled",false);
  }
  validatePasswords(password1);

}, 500));

$('#confirm_password').keyup(delay(function(e){
  password2 = this.value;
  if(!validatePasswords(password1,password2)){
    $('.cpassword').show();
    $('#btnSubmit').attr("disabled",true);
//    disableSubmit();
  }
  else{
    $('.cpassword').hide();
    $('#btnSubmit').attr("disabled",false);
  }
}, 500));

function isValidEmailAddress(emailAddress) {
  var pattern = /^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$/i;
  return pattern.test(emailAddress);
}

function isValidPW(password) {
  var minMaxLength = /^[\s\S]{8,32}$/,
      upper = /[A-Z]/,
      lower = /[a-z]/,
      number = /[0-9]/,
      special = /[ !"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~]/;

  if (minMaxLength.test(password) &&
      upper.test(password) &&
      lower.test(password) &&
      number.test(password) &&
      special.test(password)
  ) {
      return true;
  }
  return false;
}

function validatePasswords(pw1,pw2){
  return (pw1==pw2); 
}

// function disableSubmit(){
//   $("#registration-form").submit(function(e){
//     e.preventDefault();
//     $('#btnSubmit').attr("disabled",true);
//   })
// }


function delay(callback, ms) {
  var timer = 0;
  return function() {
    var context = this, args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      callback.apply(context, args);
    }, ms || 0);
  };
}

}) //document.ready