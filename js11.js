function countCharacter(str, char) {
  // your code here
  var total = 0;
  for (var x in str){
  	if (str[x] == char){
  		total += 1;
  	}
  }
  return total;
}
var output = countCharacter('I am a hacker', 'a');
console.log(output); // --> 3
