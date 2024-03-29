# one - line comment

'''
I
am 
multi-line comment
'''

# data types:
# 1. integer - (numbers without floating point/ decimal)
myInt = 6
print("MyInt var: ", myInt)
print("type: ", type(myInt), "\n")


# 2. floating point - (numbers with decimal)
myFloatPt = 5.8
print("myFloatPt var: ", myFloatPt)
print("type: ", type(myFloatPt), "\n")

# 3. string - (group of letters)
myStr = "Rhea"
print("myStr var: ", myStr)
print("type: ", type(myStr), "\n")

# 4. bool - (boolean - true/false)
myBool = True
print("myBool var: ", myBool)
print("type: ", type(myBool), "\n")


# 5. sequence - (list, tuple, range)
myList = [3, 5, 9, 1]
print("myList var: ", myList)
print("type: ", type(myList), "\n")
myList.append(19)
print("myList var: ", myList, "\n")

myTuple = (3, 9, 6, 12)
print("myTuple var: ", myTuple)
print("type: ", type(myTuple), "\n")
print("index: ", myTuple.index(6), "\n")

# range maths : [2,6] - {2, 3, 4,5, 6}
# (2, 6] - {3, 4, 5, 6} 
# [2,6) - {2, 3, 4, 5 }

#              initial value, till value, increment 
# [2, 10) - {2, 4, 6, 8}
myRange = range(2, 10, 2)
print("myRange var: ", myRange)
print("type: ", type(myRange), "\n")

for i in myRange:
    print("i : ", i)

print("\n")

# 6. set - (sequence of unique numbers)
mySet = {2, 5,5,7} # 2, 5,7
print("mySet var: ", mySet)
print("type: ", type(mySet), "\n")

# 7. map - (dict)
myDict = {1: "Rhea", 2: "Sonu", 3: "Parush"}
print("myDict var: ", myDict)
print("type: ", type(myDict), "\n")
