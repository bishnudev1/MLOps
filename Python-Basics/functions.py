#Normal Function

def add(a,b):
    return a+b

print(add(2,3))

#Lambda Function

add = lambda a,b: a+b

print(add(2,3))

#Map Function

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))

print(squared)

#Filter Function

numbers = [1, 2, 3, 4, 5]

even = list(filter(lambda x: x%2 == 0, numbers))

print(even)

#Reduce Function

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x+y, numbers)



