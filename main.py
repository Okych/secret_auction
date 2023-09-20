
import os

bids = {}
finished_bidding = False 

def find_highest_bidder(bidding_record):

    hightest_bidder = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > hightest_bidder:
            hightest_bidder = bid_amount
            winner = hightest_bidder
    print(f"the winner is {winner} and bid is {hightest_bidder}")


while  not finished_bidding:
    
    name = input("What is your name ")
    price = int(input("What is your bidding price? $ "))
    bids[name] = price
    should_continue = input("Are there other bidder? Type 'yes' or 'no' ")
    if should_continue == 'no':
        finished_bidding = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls')



