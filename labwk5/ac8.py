class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())