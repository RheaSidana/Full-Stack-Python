# modules and packages
# crud: create read update and delete 

# files - modules
# folders - packages

# adding the whole module in the current module
# import example1

# try: 
#     num = 3
#     if type(num) is not str:
#         raise example1.MyException("variable is not of type str")
# except example1.MyException as e:
#     print(e) 
# finally:     
#     print("I am finally")


# adding particular class / function / variable
from example1 import MyException, num

try: 
    # num = 3
    print("num  = ", num)
    if type(num) is not str:
        raise MyException("variable is not of type str")
except MyException as e:
    print(e) 
finally:     
    print("I am finally")

print("outside try-except-finally block")