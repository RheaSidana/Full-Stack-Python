//2. comparison operators: 
// -less than, greater than, less than and equal to, greater than and equal,.....
//3 is less than 4 -> ( 3  <  4)
// <, >, <=, >=
let var1 = 3, var2 = 6;
console.log("Greater than: ",var1 > var2); 
console.log("Less than: ", var1 < var2); 
console.log("Greater than and equal to: ", var1 >= var2); 
console.log("Less than and equal to: ", var1 <= var2); 

console.log("\n Greater than and equal to: ", var1 >= var1);
console.log("Less than and equal to: ", var1 <= var1);


// var1 == var1 -> if the var1 and var2 are having the same but of different data type -> true
// var1 === var2 -> compares the value and its data type
// let var1 = 3, var2 = 6;
console.log("typeof: ",  typeof var2);
var2 = "3";
console.log("typeof: var2",  typeof var2);
console.log("typeof: var1",  typeof var1);
// console.log("==", var1 == var1);
console.log("==", var1 == var2);
console.log("===", var1 === var2, "\n");

var2 = 3;
console.log("typeof: var1",  typeof var1);
console.log("typeof: var2",  typeof var2);
console.log("var1===var2", var1 === var2);

console.log("\n");
// var1 != var2 -> compare the values, irrespective of the data type
// ! -> not = -> equal
// let var1 = 3, var2 = 3;
console.log("!=", var1 != var2); //false
console.log("!=", var1 != 10); // true
console.log("!=", var1 != "10"); // true
console.log("!=", var1 != "3"); // false

console.log("\n");
// var1 !== var2 -> compare value and the data type
// var1 = 3, var2 = 3;
console.log("!=", var1 !== var2); // false 
console.log("!=", var1 !== 10); // true
console.log("!=", var1 !== "10"); //true
console.log("!=", var1 !== "3"); // true


