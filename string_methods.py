"""
Examples to show available string methods in python

"""

# Accessing characters in string
# index starts from zero

first = "nyc"[0]
print(first)
city = "sfo"
print(city[0])

"""
lower()
upper()
len()
str()
"""

str1 = "This is a Mixed Case "

print(str1.lower())

print(str1.upper())

print(len(str1))

# converting int to str data type
print(str1+str(2))

# string concatenation

print("Hello "+" "+" world")
print(first + " " + city)