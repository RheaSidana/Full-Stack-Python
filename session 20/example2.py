try:
    num = 3
    den = 10
    # if type(num) is not str:
    #     raise TypeError("variable is not of type str")
    res = num/den
    p = 9
    r = 55
except ZeroDivisionError as e:
    print(str(e))
    print("division by zero error occured")
except TypeError as e:
    print(str(e))
    print("inside TypeError exception")
except Exception as e:
    print(str(e))
    print("This is parent exception")
else:
    print("This block is executed when no error is thrown")
finally:
    print("This is finally block.")


print("after exception")