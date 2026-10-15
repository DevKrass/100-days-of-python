print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
n_people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100 + 1

total = bill * tip_percentage

pay = total / n_people

print(f"Each person should pay {round(pay, 2)}")
