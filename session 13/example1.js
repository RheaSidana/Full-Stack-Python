// hello world
function helloWorld() {
    console.log("Hello World");
}

helloWorld();

// function_keyword function_name ( function_parameter )
function helloUser(name){
    console.log("Hello", name, "How are you?");
}

// Hello Rhea How are you?
helloUser("Rhea");

function findGrades(marks){
    // 90<=marks<=100
    if(marks >= 90 && marks <= 100){
        return "Grade A";
        // return 1;
    }
    // 80<=marks<=89
    else if (marks >= 80 && marks <=89){
        return "Grade B";
    }
}

console.log("My grades in Maths:", findGrades(95));
console.log("My grades in Eng:", findGrades(88));