# input from the user
# name = input("Enter your name ")
# age = int(input("Enter your age "))

age = 19

# print("Hi " + name + "! You are " + age+" years old.")

if age > 18:
    print("you are adult.")
elif age < 13:
    print("you are in school.")
else:
    print("you are a teen ager.")


# loops : for, while
list = [3, 5, 7, 9, 11] 
for i in list:
    print("list item: ", i)

print("\n")

p = 0
while p < len(list):
    print("p: ", list[p])
    p+=1
