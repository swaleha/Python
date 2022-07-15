str1 = 'This is a "J.K Rowling" book'
str2 = "This is J.K Rowling's book"
str3 = """Roses are red
  Sky is blue
  God bless you"""
str4 = "Test "
str5 = "Automation"
str6 = "   Testing   "
str7 = "hello"
str8 = "HELLO"

print("****Display strings: ****")
print("String 1. "+str1)
print("String 2. "+str2)
print("String 3. "+str3)

print("\n****String concatenation: ****")
print("String 4."+str4+str5)

print("\n****Display a string multiple times: ****")
print("String 5."+str4*5)

print("\n****Substrings: ****")
print("6."+str5[0])
print("7."+str5[0:4])
print("8."+str5[2:])
print("9."+str5[:9])

print("\nLength of string 4 is : "+str(len(str4)))

print("Length of string 5 is :"+str(len(str5)))

print("Length of string 6: "+str(len(str6)))

print("\n************************************String 6.:"+str6)

print("*Remove spaces from the left side of the string 6:"+str6.lstrip())

print("Remove spaces from the right side of the string 6:"+str6.rstrip())

print("****Remove spaces from both sides of the string 6:"+str6.strip())

print("\nDisplay string in capital letters:"+str5.upper())

print("\nDisplay string in small letters:"+str5.lower())

print("\nReplace cases of letters in a string:"+str5.replace('omat','OMAT'))

print("\nPosition of the book name Rowling in the string 1 : "+str(str1.find('Rowling')))

print("\nSplit string into into a list:")
li = str2.split(" ")
print(li)

print("\nTwo strings for comparison are: "+str7+"\t"+str8)
print("*****Comparing two strings: ******")
if(str7 == str8):
    print("Strings match")
else:
    print("Strings don't match")

print("\nConvert both strings to the same case to match:")

if(str7.upper()==str8.upper()):
    print("Strings match")
else:
    print("Strings don't match")



