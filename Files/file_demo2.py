"""
File I/O
Reading a file -> .read()
Reading a file line by line -> readline()
"""

my_file = open("firstfile.txt", "r")
print(str(my_file.read()) + "\n")
my_file.close()

my_file1 = open("firstfile.txt", "r")
print(str(my_file1.readline()))
my_file1.close()
