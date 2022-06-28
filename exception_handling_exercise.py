"""
Program to demonstrate exception handling in python.
Exception is an event that disrupts the normal execution of program

"""

try:
    car = {"make":"BMW", "model":"550i", "year":2016}
    print(car["color"])
except:
    print("Key not found")
    raise Exception("Exception occurred")
finally:
    print("Please use the correct key")
