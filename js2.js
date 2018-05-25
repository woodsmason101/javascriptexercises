function userName(str){
	var answer= /^\w+[_]\d\d$/
	var second= answer.test(str);
	return second;
}
function searchPrice(str){
	var answer= /\$\d+/;
	var second= answer.exec(str);
	return second[0];
}





console.log(searchPrice('The raspberry pi cost $35 at the store.'));
console.log(userName('george_68'));
