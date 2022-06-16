"""
Examples to show available string methods in python
"""

str1 = "1abc2abc3abc4abc5abc"
print(str1.replace('abc',"ABC"))

"""

Sub strings
Starting index is inclusive
Ending index is exclusive

"""

print("\n*********************\n")

sub = str1[1:6]
step = str1[1:6:2]

print(sub)
print(step)

