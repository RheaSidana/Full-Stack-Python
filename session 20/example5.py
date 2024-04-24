def myFunc(a,b):
    return a+b #adding

def main():
    print("I am main function of example5")


print("__name__ = "+ __name__)

if __name__ == "__main__":
    main()
else:
    print("addition: ", myFunc(2, 3))