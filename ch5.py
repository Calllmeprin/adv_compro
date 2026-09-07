class Animals:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"This is an animal named {self.name}."

class Cat(Animals): #inherit from animals class
    def __init__(self, name):
        super().__init__(name) # when inherit used SUPER 

    def meow(self):
        return f"{self.name} says Meow!"
    
pinky = Cat("Pinky")    
print(pinky.info())
print(pinky.meow())