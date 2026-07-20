sqaure_func = lambda x: x*x

is_even = lambda x: x%2 == 0 

numbers=[1 ,2 ,3, 4, 5]
sqs = list (map(sqaure_func, numbers))
print(sqs)

event_numbers = list(filter(is_even, numbers))
print(event_numbers)