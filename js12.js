function convertScoreToGradeWithPlusAndMinus(score) {
  // your code here
  if (score <= 100 && score >= 90 ){
  	if (score == 100 || score ==99 || score==98){
  	return 'A+';
  	}
  	if (score == 91 || score ==92 || score==90){
  	return 'A-';
  	}
  	else{
  	return 'A';
  	}
  }
  if (score <= 89 && score >= 80 ){
  	if (score == 89 || score ==88){
  	return 'B+';
  	}
  	if (score == 81 || score ==82 || score==80){
  	return 'B-';
  	}
  	else{
  	return 'B';
  	}
  }
  if (score <= 79 && score >= 70 ){
  	if (score == 79 || score ==78){
  	return 'C+';
  	}
  	if (score == 71 || score ==72 || score==70){
  	return 'C-';
  	}
  	else{
  	return 'C';
  	}
  }
  if (score <= 69 && score >= 60 ){
  	if (score == 69 || score ==68){
  	return 'D+';
  	}
  	if (score == 61 || score ==62 || score==60){
  	return 'D-';
  	}
  	else{
  	return 'D';
  	}
  }
  if (score <= 59 && score >= 0 ){
  	return 'F';
  }
  if (score > 100 || score < 0){
  	return 'INVALID SCORE';
  }
}
var output = convertScoreToGradeWithPlusAndMinus(95);
console.log(output); // --> 'A-'
