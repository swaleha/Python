#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6 
#Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 0r 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill    # bill_with_tip = bill * (1 + (tip/100))
total_bill = bill_with_tip / people
final_bill = "{:.2f}".format(total_bill)
print(f"Each person should pay: ${final_bill}")