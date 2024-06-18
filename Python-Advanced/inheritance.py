

# Inheritance

# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).

# Consider a base class Animal with

# Methods: walk, eat

# Consider a derived class Dog with

# Methods: bark

# The derived class Dog inherits the methods of the base class Animal.

# Example:

class Animal:
    def walk(self):
        print("walk")

    def eat(self):
        print("eat")

class Dog(Animal):
    def bark(self):
        print("bark")

dog = Dog()
dog.walk()
dog.eat()
dog.bark()


# Output:

# walk

# eat

# bark

# In the above example, the derived class Dog inherits the methods of the base class Animal.

# The derived class Dog has a method bark that is not present in the base class Animal.

# The derived class Dog can access the methods of the base class Animal.

# Multiple Inheritance

# Multiple inheritance is a feature in which a class can inherit attributes and methods from more than one base class.

# Example:

class A:
    def method1(self):
        print("method1")

class B:
    def method2(self):
        print("method2")

class C(A, B):
    def method3(self):
        print("method3")

c = C()
c.method1()
c.method2()
c.method3()

