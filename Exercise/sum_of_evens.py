# Sum of even numbers from 1 to 100

total = 0
for number in range(0, 101, 2):
    total += number
print(total)

total2 = 0
for number in range(0, 101):
    if number % 2 == 0:
        total += number
print(total2)