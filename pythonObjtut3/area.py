#URL: https://kinsta.com/blog/python-object-oriented-programming/

class Shape:
    def __init__(self, side1,side2):
        self.side1 = side1
        self.side2 = side2


    def get_area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f"The area of this {self.__class__.__name__} is : {self.get_area()}"


class Square(Shape):
    def __init__(self,side):
        super().__init__(side,side)

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base,height)

    def get_area(self):
        area = super().get_area()
        return area / 2


Rec = Shape(5,5)
print(Rec.__str__())
print(Rec.get_area())

Square = Square(3)
print(Square.get_area())
print(Square.__str__())

Tri = Triangle(5,3)
print(Tri.__str__())