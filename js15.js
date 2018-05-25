function owassoRams(n){
	list=[];
  var total_sum = 0;
	for (i = 0; i < n; i++){
		total_sum += 1;
		number3= total_sum/3;
		number5= total_sum/5;
		slurp =(number3)%1===0;
  	mark =(number5)%1===0;
  	if (slurp && mark === true){
    list.push('OwassoRams');
  	}
  else{
    if (slurp===true){
      list.push('Owasso');
    }
  
    else if (mark === true){
      list.push('Rams');
    }
    else{
      list.push((total_sum));
    }
  }
	}
	return list;
}
var output = owassoRams(15);
console.log(output);
