import art

print(art.logo)


def find_highest_bidder(bid_dict):
    highest_bidder = ""
    highest_bid = 0
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder

    print(f"Highest bidder is {highest_bidder} with a bid of {highest_bid}.")


bids = {}
should_continue = True

while should_continue:
    name = input("What is your name\n").lower()
    bid = int(input("What is your bid\n"))

    bids[name] = bid
    more_bidders = input("Are there any other bidder. Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        should_continue = False
        find_highest_bidder(bids)
