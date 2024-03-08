// operators: +, -, *, /, .....
// operands: values on which the operator are applied
let a = 9, b=10;
// sum = a + b; // a and b are operands and + is an operator 

let sum = a + b;

console.log(a, " + ", b, " = ", sum);

// types of operators:
//1. arithmetic: +, -, *, / 
let c = 100;
sum = a + b + c;
console.log(a, " + ", b, " + ", c, " = ", sum);

let subtract = a - b;
console.log(a, " - ", b, " = ", subtract);
console.log(a, " * ", b, " = ", (a * b));
console.log(a, " / ", b, " = ", (a / b));
console.log(a, " ** ", 2, " = ", (a ** 2));
// 6/3 = 2, remainder = 0
console.log(6, " % ", 3, " = ", (6 % 3));  // modular  -> returns remainder
// 8 / 3 = 2, remainder = 2
console.log(8, " % ", 3, " = ", (8 % 3));  // modular 

// a = 9
console.log("A: ", a, "next value: ", a++); 
// a++ -> return a and increment a to (a+1)
// a = a+1;

// a = 10
console.log("A: ", a, "next value: ", ++a); 
// ++a -> increments a to (a+1) and then return a

// a = 11
console.log("A: ", a, "prev value: ", a--);
// a-- -> return a and decrement a to (a-1)
// a = a - 1; // a = 10;

// a = 10
console.log("A: ", a);
console.log("A: ", a, "prev value: ", --a);
// --a -> decrement a to (a-1) and return a
//a = a- 1 // a=9;

//2. comparison operators: 
//3. logical operators: 
//4. asignment operators: