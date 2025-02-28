//инструкции вида "if...else"

let a = Math.floor(Math.random() * 100);
let resultA;

if (a > 10) {
    if (a > 5) {
        resultA = 2 * a + 1;
    } else {
        if (a < 3) {
            resultA = 1;
        } else {
            resultA = 2 * (a - 2);
        }
        if (resultA > 4) {
            resultA = 5;
        } else {
            if (a % 2 == 0) {
                resultA = 6;
            } else {
                resultA = 7;
            }
        }
    }
} else {
    if (a * 2 > 5) {
        resultA = 2 * a + 1;
    } else {
        if (a < 3) {
            resultA = 1;
        } else {
            resultA = 2 * (a - 2);
        }
        if (resultA > 4) {
            resultA = 5;
        } else {
            if (a % 2 == 0) {
                resultA = 6;
            } else {
                resultA = 7;
            }
        }
    }
}

console.log(resultA);

//инструкции вида "switch()"

let b = Math.floor(Math.random() * 100);  
let resultB;  

switch (true) {  
    case (b > 10):
        switch (true) {  
            case (b > 5):
                resultB = 2 * b + 1;  
                break;  
            default:  
                switch (true) {  
                    case (b < 3):  
                        resultB = 1;  
                        break;  
                    default:  
                        resultB = 2 * (b - 2);  
                        break;  
                }  
                switch (true) {  
                    case (resultB > 4):  
                        resultB = 5;  
                        break;  
                    default:  
                        switch (true) {  
                            case (b % 2 == 0):  
                                resultB = 6;
                                break;  
                            default:  
                                resultB = 7; 
                                break;
                        }  
                }  
        }  

    default:
        switch (true) {  
            case (b * 2 > 5): 
                resultB = 2 * b + 1;  
                break;  
            default:  
                switch (true) {  
                    case (b < 3):  
                        resultB = 1;  
                        break;  
                    default:  
                        resultB = 2 * (b - 2);  
                        break;  
                }  
                switch (true) {  
                    case (resultB > 4):  
                        resultB = 5;  
                        break;  
                    default:  
                        switch (true) {  
                            case (b % 2 == 0):  
                                resultB = 6;
                                break;  
                            default:  
                                resultB = 7;
                                break; 
                        }  
                }  
        }  
}  

console.log(resultB);