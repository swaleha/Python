"""
This program demonstrates the use of while loop
while loop continues until the condition is true
break statement ends the loop and goes to next statement in the program (outside loop)
continue statement skips the current part of the loop and moves to the next part of the loop
pass statement skips any part of the loop where pass appears
"""

temp_f = 40

while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break


print("Water becomes ice at 32 degrees fahrenheit")


for number in range(1, 11):
    if number == 7:
        print("We are skipping Number 7!")
        continue
    print("Number {}".format(number))


for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The number is {}".format(number))