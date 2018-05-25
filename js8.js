function findMinLengthOfThreeWords(word1, word2, word3) {
  // your code here
  a=word1.length;
  b=word2.length;
  c=word3.length;
  if (a < b){
  	if (a < c){
  		return a;
  	}
  	if (a > c){
  		return c;
  	}
  }
  if (b<a){
  	if(b<c){
  		return b;
  	}
  	if(b>c){
  		return c;
  	}
  }
}
var output=findMinLengthOfThreeWords('a', 'be', 'see');
console.log(output);
