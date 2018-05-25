function checkAge(name, age) {
  // your code here
  if (age>=21){
  	return ("Welcome, " + name+'!');
  }
  if (age<21){
  	return ("Go home, " + name+"!");
  }
}
var output = checkAge('Adrian', 18);
console.log(output);
