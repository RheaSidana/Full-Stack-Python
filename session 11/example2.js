//3. logical operators: 
// &&, ||, !

// a = true, !a = false
// a = false, !a = true
console.log("!true", !true);

// a = true and b = true
//  a       b           a && b      a || b
// true     true        true        true
// false    false       false       false
// true     false       false       true
// false    true        false       true
console.log("3 < 5 && 7 > 5", 3 < 5 && 7 > 5);
//  1 <= x <= 10
let x=5;
console.log("x >= 1 && x <= 10", x >= 1 && x <= 10);
//          true    &&  true = true
console.log("x >=1 || x <= 4", x >=1 || x <= 4);
//          true   || false => true

// console.log("enter your name");

//4. asignment operators:
// +, - , *, /, %, ** -> arithmetic operator
console.log("\n");
let b = 3;
console.log("B: ", b);
b = b + 9;
console.log("B: ", b);
b += 1; // b = b + 1;
console.log("B: ", b);

b -= 9;
console.log("B: ", b);
b /= 2;
console.log("B: ", b);

b **= 3; // (2)^ 3 = (2 * 2 * 2 = 8)
console.log("B: ", b);

b %= 3; // 8/3 = 2, rem =2
console.log("B: ", b);