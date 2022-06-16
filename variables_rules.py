import keyword
print(keyword.kwlist)
variable_name = 10
cars = 5
_cars = 2
CARS = 3
cars2 = 15
print(variable_name)
a = b = c = 20
print(a, b, c)
print(cars,_cars,CARS,cars2)

"""
String formatting
"""

print("{}, programming is very good for beginners.".format("Python"))

str1 = "This code is written in {}"
print(str1.format("Python"))
print("My program is {} day old".format(1))