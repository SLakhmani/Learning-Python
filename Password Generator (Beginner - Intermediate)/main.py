# Password Generator
import random

# Initialize character lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user input
print("Welcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

# Initialize empty list
password_list = []

# Append randomly generated letters into existing password list 
password_list.extend(random.choices(letters, weights=None, cum_weights=None, k=nr_letters))

# Append randomly generated symbols into existing password list
password_list.extend(random.choices(symbols, weights=None, cum_weights=None, k=nr_symbols))

# Append randomly generated numbers into existing password list
password_list.extend(random.choices(numbers, weights=None, cum_weights=None, k=nr_numbers))

# Randomly shuffle the password list to make it more jumbled
random.shuffle(password_list)

# Join all the characters in the password list to form a string
password = ''.join(password_list)

# Show generated password
print("\nYour generated password is: " + password)
