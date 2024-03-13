// classes

class Employee {
  /**
     * id: "101", // string  - 2 bytes
    name: "Rhea Sidana", // string - 2 bytes
    age: 34, // number - 4 bytes
    designation: "Developer", // string - 2 bytes
    access: "Level 1", //string - 2 bytes

    Total memory required= 2+2+4+2+2 = 12
     */
  constructor(eid, ename, eage) {
    // function which helps in initialising our object,
    // by allocation memory to each object
    // called by default - by the name of the class
    this.id = eid;
    // this.id = "E_" +eid;
    this.name = ename;
    this.age = eage;
  }

  displayEmployee() {
    console.log("Name: ", this.name);
    console.log("ID: ", this.id);
    console.log("Age: ", this.age);
  }

  updateID(prefix){
    this.id = prefix + this.id;
  }
}

// function displayEmployee(employee) {
//   console.log("Name: ", employee.name);
//   console.log("ID: ", employee.id);
//   console.log("Age: ", employee.age);
// }

let myEmployee = new Employee("1", "Rhea", 30);
let myEmployee2 = new Employee("2", "Sidana", 40);
// new keyword = helps in calling the constructor
// for allocation of new memory block

// displayEmployee(myEmployee);
// displayEmployee(myEmployee2);

myEmployee.displayEmployee();
myEmployee2.displayEmployee();

// update id as E_1 : myEmployee
// update id as EMP_2 : myEmployee2
myEmployee.updateID("E_");
myEmployee2.updateID("EMP_");

console.log("\n Employee after update!!\n");
myEmployee.displayEmployee();
myEmployee2.displayEmployee();