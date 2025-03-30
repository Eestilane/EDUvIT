//инструкции вида "if...else"

function manyChecksA() {
    let a = Math.floor(Math.random() * 20) + 1;
    console.log(`a = ${a}`);
    
    let result = '';
  
    if (a > 10) {
      result += 'a is bigger than 10';
    } else {
      result += 'a is less than or equal to 10 ';
      if (a === 5) {
        result += 'an example of a special case';
      }
    }
  
    if (a === 15) {
      result += 'but a is not 15';
    }
  
    if (a > 5) {
      result += 'and a is greater than 5';
    } else {
      result += 'and a is less than or equal to 5 ';
    }
  
    if (a % 2) {
      result += ' and a is odd';
    } else {
      result += ' and a is even';
    }
  
    console.log(result);
}
  
manyChecksA();

//инструкции вида "switch()"

function manyChecksB() {
    let b = Math.floor(Math.random() * 20) + 1;
    console.log(`b = ${b}`);
    
    let result = '';
  
    switch (true) {
      case b > 10:
        result += 'b is bigger than 10';
        break;
      default:
        result += 'b is less than or equal to 10';
        break;
    }
  
    switch (b) {
      case 5:
        result += ' an example of a special case';
        break;
      case 15:
        result += ' but b is not 15';
        break;
    }
  
    switch (true) {
      case b > 5:
        result += ' and b is greater than 5';
        break;
      default:
        result += ' and b is less than or equal to 5';
        break;
    }
  
    switch (b % 2) {
      case 1:
        result += ' and b is odd';
        break;
      case 0:
        result += ' and b is even';
        break;
    }
  
    console.log(result);
}
  
manyChecksB();