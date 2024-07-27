from django import template

register = template.Library()

# filter - this will capitalize the first letter of each word in the string
@register.filter(name="capital_words")
def capital_words(value):
    if type(value) is str:
        return " ".join([words.capitalize() for words in value.split(" ")])
    return value