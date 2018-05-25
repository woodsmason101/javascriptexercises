function getLongestWordOfMixedElements(arr) {
  // your code here
  var len=0;
  var ret=0;
  var str=0;
  var run=0;
  var numlen=0;
  var list=arr.length;
 if (run < list){
 while (run <= list){
  	if (typeof arr[str] == 'number'){
  		arr[str]=('');
  		run += 1;
  		str += 1;
  	}
  	else if (typeof arr[str] == 'string'){
  		if (arr[str].length > len){
  			len = arr[str].length;
  			ret = str;
  			run+=1;
  			str+=1;
  		}
  		if (arr[str].length < len){
  			run+=1;
  			str+=1;
  		}
  	}
  	if (run == list){
  		return arr[ret];
  	}
  }
 }
 if (arr.length === 0){
	return '';
	}
}
var output = getLongestWordOfMixedElements([3, 'word', 5, 'asdfup', 3, 1]);
console.log(output); // --> 'word'
