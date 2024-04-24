import example5

def myFunc(a,b):
    return a-b # subtracting

def main():
    print("I am main function of example6")

print("__name__ = "+ __name__)

if __name__ == "__main__":
    main()
else:
    print("subtarction: ", myFunc(2, 3))