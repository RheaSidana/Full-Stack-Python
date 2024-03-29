#single inheritance
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def perimeter(self):
        return (2*(self.length+ self.breadth))

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        # self.side = side
    
    # def perimeter(self):
    #     return (4*self.length)

    def __str__(self):
        return f'Length: {self.length}'
    
mySquareObj = Square(3)
print(mySquareObj.length)
print(mySquareObj)

print("Perimeter of square: ", mySquareObj.perimeter())

myRectObj = Rectangle(3, 3)
print("Perimeter of Rectangle: ", myRectObj.perimeter())