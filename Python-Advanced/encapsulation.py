
# Encapsulation is the process of restricting access to methods and variables in a class in order to prevent direct modification of data.

# Encapsulation can be achieved by using private methods or private variables in a class. Private methods or variables are prefixed with an underscore.

# Example:

class Car:
    def __init__(self):
        self._speed = 0

    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed
    
car = Car()

car.set_speed(100)
print(car.get_speed())

# Output:

# 100
