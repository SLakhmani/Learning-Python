import random # Import the random module
	 
# Generate a random integer between 0 and 1 (both inclusive)
coin_face = random.randint(0,1)

# 1 - Heads, 0 - Tails
if coin_face == 1:
    print("Heads")
else:
    print("Tails") 
