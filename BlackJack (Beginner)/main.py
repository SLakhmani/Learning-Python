import random
from art import logo
from os import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, npc_score):
    if user_score == npc_score:
        return "It's a Draw!"
    elif npc_score == 0:
        return "You Lose! Computer has a Blackjack!"
    elif user_score == 0:
        return "You Win! You have a Blackjack!"
    elif user_score > 21:
        return "You Lose! You went over 21!"
    elif npc_score > 21:
        return "You Win! Computer went over 21!"
    elif user_score > npc_score:
        return "You Win! Your score is higher!"
    else:
        return "You Lose! You score is lower!"

def play_game():
    print(logo)
    user_cards = []
    npc_cards = []
    game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        npc_cards.append(deal_card())
    
    while not game_over:
        user_score = calculate_score(user_cards)
        npc_score = calculate_score(npc_cards)
        print(f"    Your Cards: {user_cards}. Current Score: {user_score}")
        print(f"    Computers First Card: {npc_cards[0]}")
        
        if user_score == 0 or npc_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("\nType 'h' to Hit or 's' to Stand: ").lower()
            if user_choice == 'h':
                user_cards.append(deal_card())
            else:
                game_over = True
    
    while npc_score != 0 and npc_score < 17:
        npc_cards.append(deal_card())
        npc_score = calculate_score(npc_cards)
    
    print(f"\n    Your Final Hand: {user_cards}. Final Score: {user_score}")
    print(f"    Computers Final Hand: {npc_cards}. Final Score: {npc_score}")
    print(compare(user_score, npc_score))

while input("Would You Like To Play BlackJack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play_game()
