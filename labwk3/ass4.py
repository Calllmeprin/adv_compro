numbers = [1, 2, 3, 4, 5]
modified_numbers = [n+10 if n % 2 == 0 else n-1 for n in numbers]
print(modified_numbers)

