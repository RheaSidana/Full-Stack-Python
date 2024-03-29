# class 
# class ClassName:
# person:
#       - name , age
class MyClass: 
    # __init__ - is the first function that is called 
    #           - it initializes and allocates memory to the class's object
    #          - constructor of the class
    #          - it is called explicitly
    #  self - first parameter of the __init__ funtion 
    #       - it defines or refer to the object that is initialised
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2
    
    # def printProperties(self):
    #     print("Name: ", self.prop1)
    #     print("Age: ", self.prop2)
    
    def addition(self, prop3):
        prop3 += 5
        prop3 /= 3
        if prop3 > 1:
            return self.prop1 + self.prop2 + prop3
        else: 
            return 0
    
    # prop3 cannot be accessed outside the function in which it is defined
    # because prop3 scope is inside the function 
    
    def __str__(self):
        return f'This is myClass Object \nName: {self.prop1}, \nAge: {self.prop2}'



myObject = MyClass("Rhea", 20)
# myObject.printProperties()
num2 = 5
print(num2)
print(myObject)

myObject.prop1 = "Rhea Sidana"
print(myObject)

# del myObject.prop1
del myObject 
# it just removes the object from the memory
# uninitialising the properties
# it delocates the object  from the memory
# opposite of the __init__ function of the class
print(myObject)

myObj2 = MyClass("Seema", 30)
# myObj2.printProperties()
print(myObj2)

myObj3 = MyClass(3, 4)
v = myObj3.addition(3) # 3+4+3 = 10
print("Obj3 addition(): ", v)