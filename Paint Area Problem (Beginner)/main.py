# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
import math

# function definition
def paint_calc(height, width, cover):
    num_cans = math.ceil((height * width)/cover)
    return num_cans

# Get user input 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

# Using pre-definied function
num_cans = paint_calc(height=test_h, width=test_w, cover=coverage)

print(f"You'll need {num_cans} cans of paint.")
