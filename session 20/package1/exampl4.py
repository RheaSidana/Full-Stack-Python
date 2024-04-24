print("I am in custom package's module")

class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'