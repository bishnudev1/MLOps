# import sys

# a = []

# print(sys.getrefcount(a))

# b = a

# print(sys.getrefcount(a))

# c = b

# print(sys.getrefcount(a))

# del b

# print(sys.getrefcount(a))

# del c

# print(sys.getrefcount(a))

# del a

# print(sys.getrefcount(a))

# # 2

import gc

class Object:
    def __init__(self):
        print('Object created')

    def __del__(self):
        print('Object deleted')


obj1 = Object()
obj2 = Object()

obj1.ref = obj2
obj2.ref = obj1

del obj1

gc.collect()
