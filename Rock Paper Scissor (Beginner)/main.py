import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Moves list
moves = [rock, paper, scissors]
validate = False

# Ask users move
user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Generate random index for computers move
computer_move = random.randint(0,2)

# Validate user move
if user_move >= 0 and user_move <= 2:
  validate = True
  print("\nYour Move:\n")
  print(moves[user_move])

  print("\nComputer Move:\n")
  print(moves[computer_move] + "\n")
else:
  print("\nInvalid move.")

# Decide Game conclusion
if validate:
  if user_move == computer_move:
    print("It's a draw!")
  elif user_move == 0 and computer_move == 2:
    print("You win!")
  elif computer_move == 0 and user_move == 2:
    print("You lose.")
  elif computer_move > user_move:
    print("You lose.")
  else:
    print("You win!")
