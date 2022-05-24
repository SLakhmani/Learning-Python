from art import logo
print(logo + "\n\n")

bids = {}
continue_program = 'y'

while continue_program == 'y':
    bidder_name = input("What is the name of the bidder?: ")
    bid = int(input("What is the bid?: £"))

    bids[bidder_name] = bid

    print("Bid made!\n")    
    continue_program = input("Is there another bidder? 'y' for yes / 'n' for no: ").lower()
    
highest_bid = 0
highest_bidder = ""
for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder = key

print(f"The winner of the auction is {highest_bidder} with a bid of £{highest_bid}!")
