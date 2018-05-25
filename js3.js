function zipCode(str){
	var answer= /^\d{5}$/;
	var second= answer.test(str);
	return second;
}
function whiteSpace(str){
	answer= /\s/i
	return answer.test(str);
}
function socialSecurityNumber(str){
	var answer= /^\d{3}-\d{2}-\d{4}$/;
	var second= answer.test(str);
	return second;
}
console.log(zipcode(12345));
console.log(whitespace('Hi, I\'m muffin, please kill me'));
console.log(whitespace('hiimmuffinpleasekillme'))
console.log(socialsecurity('555-55-5555'));
console.log(socialsecurity('555555555'));
