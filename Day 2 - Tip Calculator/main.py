print("Welcome to the Tip Calculator.")

total_bill = float(input("What was the total bill? $"))
num_of_people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip = (total_bill * tip_percent) / 100
bill_for_each = round((total_bill + tip) / num_of_people, 2)

print(f"Each person should pay: ${bill_for_each}")