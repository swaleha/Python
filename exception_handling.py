"""
Exception is an event that occurs during execution of a program and disrupts the flow
"""

def exceptionHandling():

    try:
        a = 10
        b = "str"
        c = 0

        d = (a + b) / c
        print(d)

    except ZeroDivisionError:
        print("Zero division")

    except TypeError:
        print("Can't add string to integer")


exceptionHandling()
