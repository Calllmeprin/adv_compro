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


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rect")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._name = "Square"


Shape._count = 0  # reset so IDs start at 0


def make_shape(kind, *args):
    try:
        if kind == "rect":
            return Rectangle(*args)
        elif kind == "square":
            return Square(*args)
        else:
            raise TypeError("unknown kind")
    except TypeError as error:
        print("error:", type(error).__name__)
        return None


rectangle = make_shape("rect", 2, 3)
square = make_shape("square", 4)
unknown = make_shape("triangle", 1, 2)

print(rectangle.label())
print(square.label())
print(unknown)

def total_area(shapes):
    return sum(shape.area() for shape in shapes)


items = [
    make_shape("rect", 2, 3),
    make_shape("square", 4),
    make_shape("triangle", 1, 2),
]

shapes = [shape for shape in items if shape is not None]
print([shape.label() for shape in shapes])
print("Total:", total_area(shapes))