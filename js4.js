function cToF(celsius) {
var far = ((celsius *1.8)+32 );
console.log(celsius + '\xB0 ' + 'C ' + 'is ' + far + '\xB0 ' + 'F.');
}

function fToC(fahrenheit) {
var cel = ((5/9) * (fahrenheit - 32));
console.log(fahrenheit + '\xB0 ' + 'F ' + 'is ' + cel + '\xB0 ' + 'C.');
}

cToF(60);
fToC(45);
