class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"


dog = Dog("Buddy", "Golden Retriever")
print(dog.name)
print(dog.breed)
print(dog.speak())
