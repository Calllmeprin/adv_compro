#is_correct = True if 3>2  else False 
is_correct = "Yes" if 1<2 else "No"
print(is_correct)

numbers = [1, 2, 3]
#squares = [n*2 for n  in numbers] 
#squares = ["even" if n % 2 else "odd" for n in numbers]
#squares = ["Yes" if n == 2 else "No" for n in numbers]
squares = [n for n in numbers if n == 2]

print(numbers)
print(squares)
