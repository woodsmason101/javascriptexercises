function computeSumBetween(num1, num2) {
  // your code here
  var total=0;
  for (x = num1; x < num2; x++){
  	total+=x;
  }
  return total;
}
var output = computeSumBetween(2, 5);
console.log(output); // --> 9
