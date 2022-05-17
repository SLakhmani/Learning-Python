# Note: random.choice() is a better option however, we are only learning basics for now

import random # Import random module

# Take user input
names_string = input("Enter everybody's names, separated by commas. ")

# Split the user input uaing "," as the separator
# This creates a list with just the names which are stored in a list
names = names_string.split(", ")

# Generate a random number between 0 and 1 less than number of items in the list
# Note: Indexing begins from 0 in Python
# Eg. if there are 4 elements in the list, the last index should be 3 (0,1,2,3)
chosen_index = random.randint(0, len(names) - 1)

print(f"{names[chosen_index]} is going to buy the meal today!")
