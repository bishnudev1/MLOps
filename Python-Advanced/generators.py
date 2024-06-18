
# Generators in Python are a way to create iterators.

# There are two terms involved when we discuss generators.

# 1. Generator-Function: A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.

# 2. Generator-Object: Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop (as shown in the above example).

# Example:

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# It returns an object but does not start execution immediately.

a = my_gen()

# We can iterate through the items using next() function.

print(next(a))

print(next(a))

print(next(a))