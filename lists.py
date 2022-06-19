fruits = ["peaches", "pears", "apples", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)
fruits.append("oranges")
print(fruits)

fruits.extend(years)

print(fruits)


fruits.remove('oranges')
print(fruits)


years.pop(0)
print(years)

fruits.pop(-1)
print(fruits)

numbers = [4, 1991, 5, 18, 45, 73.56, 99.33]
numbers.sort()
print(numbers)


print("apple" in fruits)
print("apples" in fruits)

print(fruits.count("apple"))
print(fruits.count("apples"))

print(fruits.index('apples'))