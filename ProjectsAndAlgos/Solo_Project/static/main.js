$(document).ready(function() {
console.log('working in jquery');

$('#fn').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if (this.value.length < 2){
    $('.fn').removeClass('hidden');
  }
  if (this.value.length >=2 ){
    $('.fn').addClass('hidden');
  }
}, 500));

$('#ln').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if (this.value.length < 2){
    $('.ln').removeClass('hidden');
  }
  if (this.value.length >=2 ){
    $('.ln').addClass('hidden');
  }
}, 500));

$('#email').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if( !isValidEmailAddress( this.value ) ) { 
    $('.email').removeClass('hidden');
  }
  else{
    $('.email').addClass('hidden');
  }
}, 500));

$('#password').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if( !isValidPW( this.value ) ) { 
    $('.password').removeClass('hidden');
  }
  else{
    $('.password').addClass('hidden');
  }
}, 500));

$('#confirm_password').keyup(delay(function(e){
  console.log('on keyup function');
  console.log('time elapsed!',this.value);
  if( ( this.value ) != $('#password').value ) { 
    $('.cpassword').removeClass('hidden');
  }
  else{
    $('.cpassword').addClass('hidden');
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

})