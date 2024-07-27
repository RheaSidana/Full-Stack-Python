def capital_words(value):
    if type(value) is str:
        return " ".join([words.capitalize() for words in value.split(" ")])
    return value    


print(capital_words("i am rhea"))
print(capital_words(10))