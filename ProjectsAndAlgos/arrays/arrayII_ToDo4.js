//faster factorial
function factorial(num){
  if (num == 0){
    return 1;
  }
  return num * factorial(num - 1);
}
//fancy fibonacci
function fancyFib(num){
  if (num == 0){
    return 0;
  }
  if (num ==1){
    return 1;
  }
  if (num ==2){
    return 1;
  }
  if (num ==3){
    return 2;
  }
  return fancyFin(num - 1) + fancyFib(num - 2);
}