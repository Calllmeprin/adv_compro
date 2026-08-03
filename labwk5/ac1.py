class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}."

r1 = Robot("Robo")
print(r1.introduce())