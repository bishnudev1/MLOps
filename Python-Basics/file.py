
# Read a file

# To read a file in Python, you can use the open() function with the 'r' mode. The open() function returns a file object that you can use to read the contents of the file.

# Syntax:

# file = open("file_name", "r")

with open("example.txt", "r") as file:
    print(file.read())

# Output:

# Hello, World!

# This is an example file.

# The read() method reads the entire contents of the file and returns it as a string.

# Read a file line by line

# To read a file line by line in Python, you can use a for loop to iterate over the file object.

# Syntax:

# file = open("file_name", "r")

# for line in file:

#     print(line)

with open("example.txt", "r") as file:
    for line in file:
        print(line)

# Write to a file

with open("hello.txt",'w') as writeFile:
    writeFile.write("Hello,all")