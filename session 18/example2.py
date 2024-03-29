# operators
# 1. Arithmetic Operators: +, - , *, /, **, %
# 2. Assignment Operators: -=, +=, *=, /=, %=, //= (divide - floor), 
#     bitwise (1,0): &= (and), != (or), ^= (xor), >>= (right-shift) , <<= (left-shift)
# no1 =1  , no2 = 2 - > no1 &= no2
# 001, 010 - & => 000

#  a     b      xor
# true  false   true
# false true    true
# false false   false
# true  true    false


# >>=, 3 => 011, 5
# 0 -> 011  => 001
# 0 -> 001 => 000 = (0)

# 5 => 101, 3
# 0 -> 101 = 010 (2)
# 0 -> 010 = 001 (1)
# 0 -> 001 = 000
a= 5
b= 1
a >>= b
print(a)

# <<=

# Comparison Operator: >, < >=, <= 
# Logical: and, or, not - truth table
# Bitwise Operator: &, |, ^, !, << , >>
# Membership Operator: in, not in
list = [4, 6]
print(4 in list)
print(4 not in list)

# Indentity Operator: is, is not
print("rhea" is "rhea")
no1 = 3
no2 = 5
print(no1 is no2)
print(no1 is not no2)