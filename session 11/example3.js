// control statements/ structures

// if else
let age = 15; // teen age
if (age >= 18) {
  // false
  console.log("Person is an adult");
  console.log("Person is an adult");
  console.log("Person is an adult");
}
// else if (age === 15) //true
// {
//     console.log("Person is 15yrs old");
// }
else if (age >= 13 && age <= 18) {
  // true
  console.log("Person is in their teenage");
  if (age === 15) {
    //true
    console.log("Person is 15yrs old");
  }
} else {
  console.log("Person is not an adult");
}

console.log("\nAfter if-else statement");

age = 18;
switch(age){
    case 15: 
        console.log("I am 15yrs old");
        console.log("I am 15yrs old");
        console.log("I am 15yrs old");
        break; // break statement 
    case 18: 
        console.log("I am 18yrs old");
        console.log("I am 18yrs old");
        console.log("I am 18yrs old");
        // break; // break statement 
        
    case 13: 
        console.log("I am 13yrs old");
        console.log("I am 13yrs old");
        console.log("I am 13yrs old");
        break; // break statement 
    default: 
        console.log("I am default");
        console.log("Person is not an adult");
}

console.log("\nAfter switch block");