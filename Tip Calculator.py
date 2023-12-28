print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $ ")) 
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = bill * (percentage / 100)
person_pay = (bill + tip) / people
print("Each person should pay: $" + str(round(person_pay, 2)))