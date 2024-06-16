print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n$"))

tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?\n"))

people = int(input("How many people to split the bill?\n"))

total = bill * ((tip_percentage/100)+1)
bill_split = total/people
final_amount = round(bill_split, 2)

print(f"Each person should pay: ${final_amount}")