function countVowels(str){
	var answer= /[aeiou]/g;
	var second= str.match(answer);
	return second.length;
}
function animalCount(str){
	var answer= /dog | cat | chicken/g;
	var second= answer.test(str);
	return second;
}
console.log(animalCount('My dog is named Jazmine'));
console.log(countVowels('hello'));
