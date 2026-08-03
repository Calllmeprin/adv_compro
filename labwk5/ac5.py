class Account:
    def __init__(self):
        self.owner = "Alice" # public
        self._branch = "ลาดกระบัง" # protected-style by convention
        self.__balance = 1000 # private-style (name mangling)


a = Account()
print(a.owner)
print(a._branch)
# print(a.__balance) # What happens if this line is enabled?
