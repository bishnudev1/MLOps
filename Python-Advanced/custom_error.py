

class dobException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    

class customError:
    def __init__(self, name, age):
        if age < 18 or age > 60:
            raise dobException("Age should be between 18 and 60")
        self.name = name
        self.age = age
            
        def display(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")

try:
    c = customError("John", 65)
    c.display()
except dobException as e:

    print(e)