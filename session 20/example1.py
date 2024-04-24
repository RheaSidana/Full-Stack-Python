# error and exception
# error: syntax error or logical error 
num = 3
num += 5 # num = num + 5
# num =+ 5

# print(num)
# print(len('hello') == 5)

# logical error : divide by zero
# num = 3
den = 0
# res = num / den

# print(res)


# errors that occur at runtime are known as Exceptions
# exception types: 
# 1. Built-in / Pre-defined exception - these exceptions are 
#       provided by the
#       python language itself
# print( dir(locals()['__builtins__']) )


# 2. Custom Exception - programmer defines these exceptions 
#       according to the requirements of the program

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__ (self):
        return f"{self.message}"
