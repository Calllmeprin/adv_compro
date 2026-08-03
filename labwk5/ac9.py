class Shape:
    _count = 0

    def __init__(self, name):
        self._name = name
        self.__id = Shape._count
        Shape._count += 1

    @property
    def id(self):
        return self.__id

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def label(self):
        return f"{self._name}#{self.id}"


shape = Shape("Shape")
print(shape.label())

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rect")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(2, 3)
print(rectangle.label())
print(rectangle.area())

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._name = "Square"


square = Square(5)
print(square.label())
print(square.area())