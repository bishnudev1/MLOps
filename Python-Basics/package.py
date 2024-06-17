
#Package

#A package is a collection of modules. It must contain an __init__.py file as a flag so that the Python interpreter processes it as such.

# Random package

# The random package is a built-in package in Python that is used to generate random numbers. It contains various functions to generate random numbers, shuffle sequences, and select random items.

# Example:

# # Import the random package

import random

# # Generate a random number between 1 and 10

x = random.randint(1, 10)

print(x)

# # Shuffle a list

fruits = ["apple", "banana", "cherry"]

random.shuffle(fruits)

print(fruits)

# # Select a random item from a list

x = random.choice(fruits)

print(x)