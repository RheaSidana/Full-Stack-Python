#  regex - Regular Expression 
# password - 1 upper case Character [A-Z]
#            1 lower case character [a-z]
#            1 special character [@, # ,$, % ....]
#            1 number [0-9]
#           length should be between 8-12 / atleast 8 char long

# "I am Rhea Sidana" -> all words in string - split wherever 
# you find the space 
# ["I", "am", "Rhea", "Sidana"]

# import re

# txt = "The rain in a Spain"
# x = re.findall("ai", txt)
# print(x)

# # ["ai","ai"]

# import re

# txt = "The rain in Spain"
#     #  012345678
# # x = re.search("\s", txt)
# x = re.search("ain", txt)
# # (5, 8) - [567]

# print("all x")
# print(x.span()) 
# # returns the start and end position of 
# # the substring that is we are searching in the original string

# #  (2, 6) - [2 3 4 5] 
# #  (3, 4) - [3]

# print("The first white-space character is located in position:", x.start())

# import re

# txt = "The rain in Spain"
# x = re.split('\s', txt)
# print(x)

# # ["The", "rain","in","Spain"]

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# "The9rain9in9Spain"