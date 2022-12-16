from auction_art import logo

print(logo)

bidders = {}

def find_highest_bidder(bidders):
    max_bid = 0
    winner = ""
    for key in bidders:
        if bidders[key] > max_bid:
            max_bid = bidders[key]
            winner = key

    print(f"{winner} won the auction with ${max_bid} bid.")

people_left = True
while people_left:
    bidder = input("What is your name? : ")
    bid = int(input("What's your bid? : $"))
    bidders[bidder] = bid
    answer = input("Are there any more bidders? Type 'yes' or 'no' : ")
    if answer == "no":
        people_left = False

find_highest_bidder(bidders)

