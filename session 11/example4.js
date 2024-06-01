// loops 
// for, while, do-while

let word = "apple";
// 3 times in a string
for(let n = 0; n < 3; n++) // n=0; n=1, n=2, n=3 
{
    console.log(word);
}

console.log("\nAfter for loop.")
for(let n = 0; n > 3; n++) // n=0
{
    console.log(word);
}

console.log("\nAfter for loop.")
// n = n+2
// initialising, condition, incrementing / decrement
for(let n = 0; n < 3; n+=2) // n=0, n=2, n=4
{
    console.log(word);
}

console.log("\nAfter for loop.")

//for(let n = 0; n < 3; n++)
//while loop 
let n=0; // initialisation
while(n<3) // condition 
{
    console.log(word); // execution statement

    n++; // increment or decrement
}

console.log("\nAfter While Loop.");