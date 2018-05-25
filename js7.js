function isEvenAndGreaterThanTen(num) {
  // your code here
  if (num>=10&&num%2===0){
  	return true;
  }
  if (num<10||num%2!==0){
  	return false;
  }
}
var output = isEvenAndGreaterThanTen(12);
console.log(output);
