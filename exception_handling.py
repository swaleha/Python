"""
Exception is an event that occurs during execution of a program and disrupts the flow
"""


def exception_handling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    # except ZeroDivisionError:
    # print("Zero division")

    # except TypeError:
    # print("Can't add string to integer")
    except:
        print("You are the in the except block")
        raise Exception("This is an exception")
    else:
        print("There is no exception so else block executes")
    finally:
        print("Finally block always executes regardless of the exceptions")


exception_handling()
