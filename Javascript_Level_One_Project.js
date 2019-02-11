var name1 = prompt('Enter your first name: ');
var name2 = prompt('Enter your last name: ');
var age = prompt('Enter your age : ');
var height = prompt('Enter your height in cm: ');
var pet = prompt('Enter your pet name: ');

if ((name1[0] === name2[0]) && (age>=20 && age<=30) && (height>=170) && (pet[pet.length-1] === 'y')) {
  console.log('I\'m batman');
}else {
    console.log('Nice try');
  }
