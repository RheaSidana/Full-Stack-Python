// arrays, objects, set, map
// arrays is a collection of element that are or not of same data type
let basket = ["pineapple", "apple", "mango", "mango"];

console.log(basket);
let sortedArray = basket.sort();
console.log(sortedArray);

let newArr = new Array(22,9,11,13,7,6,8);
// console.log(newArr.sort(function(a, b){return a-b})); // asc
// console.log(newArr.sort(function(a, b){return b-a})); // desc

newArr.push(33); // adding element at the end
console.log(newArr);
// console.log(newArr.sort(function(a, b){return b-a})); // desc

console.log(newArr.length);
console.log(newArr.pop()); // removes element from the end
console.log(newArr);


// objects is a real world entity which is having a set of property.
let employee1 = {
    id: "101",
    name: "Rhea Sidana",
    age: 34,
    designation: "Developer",
    access: "Level 1",
}

let employee2 = {
    id: "102",
    name: "NAme 2",
    location: "Delhi"
}

console.log("Employee 1: ", employee1);
console.log("Employee 2: ", employee2);

// set is a collection of unique elements
let userIDs = new Set(["user1", "user2", "user2"]);

console.log(userIDs);
// map is a collection of key-value pair, where key is always unique.
//      collection of emails -> user name
//      collection of employees, emp_id -> employee name 
let myUserMap = new Map([
    ["user1", "Sam"],
    ["user2", "Sandy"],
    ["user2", "Micheal"],
])

console.log(myUserMap);