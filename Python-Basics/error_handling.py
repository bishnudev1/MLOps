

# Error Handling

# Error handling is the process of catching errors that might occur in your program and taking appropriate action to handle them.

# Python provides a way to handle errors using try and except blocks.

# Syntax:

a = 10

b = 0

try:
    
    c = a/b

except ZeroDivisionError:
        
        print("Division by zero is not allowed")

except Exception as e:
    
    print(e)

# Output:

# Division by zero is not allowed

