
# Inbuilt Data Structures in Python

# 1. List

# A list is a collection of items that are ordered and changeable. Lists are defined by square brackets.

# Syntax:

# list_name = [item1, item2, item3]

# Example:

# # Create a list

fruits = ["apple", "banana", "cherry"]

print(fruits)

# # Access an item

print(fruits[1])

# # Change an item

fruits[1] = "orange"

print(fruits)

# # Loop through a list

for fruit in fruits:

    print(fruit)

# # Check if an item exists

if "apple" in fruits:

    print("Yes, apple is in the fruits list")

# # Get the number of items in a list

print(len(fruits))

# # Add an item

fruits.append("mango")

print(fruits)

# # Insert an item

fruits.insert(1, "grapes")

print(fruits)

# # Remove an item

fruits.remove("apple")

print(fruits)

# # Remove the last item

fruits.pop()

print(fruits)

# # Remove an item by index

fruits.pop(1)

print(fruits)

# # Copy a list

fruits_copy = fruits.copy()

print(fruits_copy)

# # Join two lists

vegetables = ["carrot", "potato", "cabbage"]

food = fruits + vegetables

print(food)

# # Clear a list

fruits.clear()

print(fruits)

# 2. Tuple

# A tuple is a collection of items that are ordered and unchangeable. Tuples are defined by round brackets.

# Syntax:

# tuple_name = (item1, item2, item3)

# Example:

# # Create a tuple

fruits = ("apple", "banana", "cherry")

print(fruits)

# # Access an item

print(fruits[1])

# # Loop through a tuple

for fruit in fruits:

    print(fruit)

# # Check if an item exists

if "apple" in fruits:
    
        print("Yes, apple is in the fruits tuple")

# # Get the number of items in a tuple

print(len(fruits))

# # Join two tuples

vegetables = ("carrot", "potato", "cabbage")

food = fruits + vegetables

print(food)

# 3. Set

# A set is a collection of items that are unordered and unindexed. Sets are defined by curly brackets.

# Syntax:

# set_name = {item1, item2, item3}

# Example:

# # Create a set

fruits = {"apple", "banana", "cherry"}

print(fruits)

# # Access an item

# Since sets are unordered, you cannot access items by index.

# # Loop through a set

for fruit in fruits:
         
        print(fruit)

# # Check if an item exists

if "apple" in fruits:
      
        print("Yes, apple is in the fruits set")

# # Get the number of items in a set

print(len(fruits))

# # Add an item

fruits.add("mango")

print(fruits)

# # Remove an item

fruits.remove("apple")

print(fruits)

# # Clear a set

fruits.clear()

print(fruits)

# 4. Dictionary

# A dictionary is a collection of items that are unordered, changeable, and indexed. Dictionaries are defined by curly brackets.

# Syntax:

# dictionary_name = {key1: value1, key2: value2, key3: value3}

# Example:

# # Create a dictionary

person = {
        
        "name": "John",
        
        "age": 30,
        
        "city": "New York"
    }


print(person)

# # Access a value

print(person["name"])

# # Change a value

person["age"] = 40

print(person)

# # Loop through a dictionary

for key, value in person.items():
        
            print(key, value)

# # Check if a key exists

if "name" in person:
            
            print("Yes, name is one of the keys in the person dictionary")

# # Get the number of items in a dictionary

print(len(person))


# # Add an item

