print("Welcome to the Tip Calculator!\n")

# Taking necessary inputs and converting types
bill = float(input("What is the total bill? £"))
tip_percentage = int(input("Enter tip percentage (10,12 or 15): "))
num_people = int(input("How many people are splitting the bill?: "))

# Calculating payment per person
bill_per_person = (bill + (tip_percentage/100)*bill)/num_people

# Formatting result to 2 decimal places
print(f"\nEach person has to pay £{bill_per_person:.2f}")
