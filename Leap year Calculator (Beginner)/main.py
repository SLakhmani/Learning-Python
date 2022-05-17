# Take user input
year = int(input("Which year do you want to check? "))

# Check if year is leap year or not

# Check if year is evenly divisible by 4
if year % 4 == 0:
  
    # Year is divisible by 4
    # Leap year if year is not divisible by 100 or divisible by both 100 and 400  
    if (year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        print("Leap year.")
    else:
        # Year is divisible by 4, divisible by 100 but not divisible by 400
        print("Not leap year.")
else:
    # Year is not divisible by 4
    print("Not leap year.")
