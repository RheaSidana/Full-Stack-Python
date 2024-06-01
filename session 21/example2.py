# decorators 
# 1. predefined function - called in custom function
# 2. assigning a function to the variable -> 
#           this variable is used to call the function
# 3. pass a particular function to the a function as parameter 
# 4. return a function from a function

# 1. predefined function - called in custom function
#  custom function
def myCustomFunction(a):
    x = a.upper()
    # change the characters to uppercase 
    print(x)

myCustomFunction("Rhea")

# 2. assigning a function to the variable -> 
#           this variable is used to call the function
toUpperCase = myCustomFunction

toUpperCase("Sidana")

# 3. pass a particular function to the a function as parameter 
def myAnotherCustomFunction(func):
    print("Hello ")
    func("Rhea Sidana")
    print("Welcome!!")

myAnotherCustomFunction(myCustomFunction)
