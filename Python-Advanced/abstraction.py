
# Abstract class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "woof"
    

class Cat(Animal):
    def speak(self):
        return "meow"
    

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
    