

# Polymorphism

# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

# Suppose, we need to color a shape, there are multiple shapes (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

# Polymorphism is based on the greek words Poly (many) and morphism (forms). We will create a structure that can take or use many forms of objects.

# Polymorphism can be carried out through inheritance, with derived classes making use of base class methods or overriding them.

# Example:

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def speak(self):
        return "meow"
    
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Output:

# woof