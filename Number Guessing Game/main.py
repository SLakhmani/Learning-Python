import random

def play_game():
    print("Welcome to the number guessing game!".title())
    print("I'm thinking of a number between 1 and 100.\n")
    difficulty = input("Choose Difficulty: Type 'easy' or 'hard': ").lower()
    
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
        
    selected_num = random.randint(1,100)
    win = False
    
    while attempts > 0 and win == False:
        print(f"\nAttemps Remaining: {attempts}")
        user_guess = int(input("Make a guess: "))
        attempts -= 1
        
        if user_guess < selected_num:
            print("Too Low. Try Again!")
        elif user_guess > selected_num:
            print("Too High. Try Again!")
        else:
            win = True
    
    if win:
        print("\nCongrats, You Win!")
    else:
        print("\nSorry, You Lose!")
    

while(input("Would You Like To Play? Type 'y' or 'n': ").lower() == 'y'):
    play_game()
