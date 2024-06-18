

# Decorators are a way to modify or extend the behavior of functions or methods without permanently modifying the function or method itself.

# Decorators have their own syntax, using the @ symbol, which is placed on the line above the function definition. The decorator is then followed by the function that will be modified.

# Example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():

    print("Hello!")

call = my_decorator(say_hello)

call()

# Output:

# Something is happening before the function is called.

# Hello!

# Something is happening after the function is called.


# Closure is a nested function which has access to a free variable from an enclosing function that has finished its execution.

# Example:

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

my_func = outer_function("Hello!")

my_func()

# Output:

# Hello!
