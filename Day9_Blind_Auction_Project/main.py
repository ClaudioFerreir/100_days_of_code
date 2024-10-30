import art

print(art.logo)
print("Welcome to the secret auction program.")

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    best_bidder = None
    highest_bid = 0

    for key in bidding_dictionary:
        if bidding_dictionary[key] > highest_bid:
            best_bidder = key
            highest_bid = bids[key]

    print(f"The winner is {best_bidder} with a bid of ${highest_bid}.")

# TODO-1: Ask the user for input
bids = {}
should_continue = True

def blind_auction():
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price
    # TODO-3: Whether if new bids need to be added

while should_continue:
    blind_auction()
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if should_continue == "no":
        should_continue = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)


