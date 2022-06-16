
int_num = 10
float_num = 20.0
print("\nInteger and Floating point number: int_num = ", int_num, ";","float_num = ", float_num,"\n")
int_num += 10
print("int_num += 10:", int_num)

int_num -= 10
print("int_num -= 10:", int_num)

int_num *= 10
print("int_num *= 10:", int_num)

int_num /= 10
print("int_num /= 10:", int_num)


a = 10.0
b = 20.0

print("\n*****Basic calcutions*****\n")

add = a + b
print("Addition: "+str(add))

sub = b - a
print("Subtraction: "+str(sub))

mul = a * b
print("Multiplication: "+str(mul))

div = a / b
print("Division: "+str(div))

rem = a % b
print("Remainder of division: "+str(rem))

print("\n*****Arithmetic operators order of precedence:*****\n")

print(" 2 + 4 * 3 / (2 + 1) = ",2 + 4 * 3 / (2 + 1))