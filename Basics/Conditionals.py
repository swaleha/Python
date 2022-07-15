"""
This program is used to show the usage of 
conditional statements and comparison operators in Python
"""

name = input("What is your name?")
if(name == "Jane"):
    print("Hello, Nice to see you {}".format(name))
elif(name == "Danielle"):
    print("Hello you are a great person!")
elif(name == "Natasha"):
    print("Hi {}, let's have lunch soon!".format(name))
else:
    print("Have a nice day!")

lug_weight = int(input("How much does your luggage weigh?"))

if(lug_weight < 20):
    print("No baggage fee")
elif(lug_weight >= 20):
    print("Please pay the baggage fee")

