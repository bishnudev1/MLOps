

# Class in Python

# A class is a blueprint for creating objects. It defines the properties and behaviors of objects.

# Syntax:

class Math:
        
        def add(self, a, b):
            
            return a + b
        
        def subtract(self, a, b):
            
            return a - b
        
        def multiply(self, a, b):
            
            return a * b
        
        def divide(self, a, b):
            
            return a / b
        
        # Constructor

        def __init__(self):
                
                print("Object created")
        

math = Math()

print(math.add(10, 5))

print(math.subtract(10, 5))

print(math.multiply(10, 5))

print(math.divide(10, 5))


# Bank Account Class

class BankAccount:
            
            def __init__(self, name, balance):
                    
                    self.name = name
                    
                    self.balance = balance
                    
            def deposit(self, amount):
                    
                    self.balance += amount
                    
            def withdraw(self, amount):
                    
                    if self.balance >= amount:
                            
                            self.balance -= amount
                            
                    else:
                            
                            print("Insufficient balance")
            
            def get_balance(self):
                    
                    return self.balance
            
            def get_name(self):
                    
                    return self.name
            
            def __str__(self):
                    
                    return f"Name: {self.name}, Balance: {self.balance}"
            

account = BankAccount("John", 1000)

print(account)

account.deposit(500)

print(account)

account.withdraw(2000)

print(account)

print(account.get_balance())

print(account.get_name())


