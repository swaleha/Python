G = 125
def printData():
	"This function prints data"
	print("**********Basic calculator**********")
	print(G)

	
def addition(a, b):
	"This function performs addition of two numbers"
	c = a + b
	print("\n")
	print("Sum of two numbers is:"+str(c))
	
	
def subtraction(a, b):
	"This function performs subtraction of two numbers"
	c = a - b
	return c
	
def multiplication(a, b = 2.5):
	"This function performs multiplication of two numbers"
	c = a * b
	print("Product of two numbers is:"+str(c))
	

def division(a, b):
	"This function performs division of two numbers"
	c = a / b
	print("Quotient is:"+str(c))
	
def modulus(a, b):
	"This function performs modulus of two numbers"
	c = a % b
	print("Remainder is:"+str(c))
	
printData()
addition(10, 20)
z = subtraction(b = 100, a = 50)
print("Difference is: "+str(z))
multiplication(float(z), 100)
division(3, 6)
modulus(5, 3)