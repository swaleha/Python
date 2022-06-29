"""
With / As keywords
"""

# print("Write function starts")
# my_write = open("textfile.txt", "w")
# my_write.write("Hello, how are you?")
# my_write.close()
#
# print("\nRead function starts")
# my_read = open("textfile.txt", "r")
# print(str(my_read.read()))

print("\nWrite function using \'With As keyword\' starts ")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of \'with as\' ")


print("\nRead function using \'With As keyword\' starts ")

with open("withas.txt", "r") as with_as_read:
    print(with_as_read.read())