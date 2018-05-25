function computeSummationToN(n) {
  // your code here
  var total = 0;
  for (x = 1; x <= n; x++){
  	total+=x;
  }
  return total;
}
var output=computeSummationToN(6);
console.log(output);
