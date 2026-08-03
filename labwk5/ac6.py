class Shape:
    def __init__(self, shape_id):
        self.__id = shape_id

    @property
    def id(self):
        return self.__id


shape = Shape(7)
print(shape.id)