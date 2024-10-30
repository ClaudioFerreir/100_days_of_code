import art

print(art.logo)
print("Welcome to the secret auction program.")
# TODO-1: Ask the user for input
bid_list = {}
other_bid = True

def blind_auction():
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $ "))
    # TODO-2: Save data into dictionary {name: price}
    bid_list[name] = price
    # TODO-3: Whether if new bids need to be added

while other_bid:
    blind_auction()
    other_bid = input("Are there any other bidders? Type 'yes' or 'no':")
    if other_bid == "no":
        other_bid = False
    print("\n" * 20)


# TODO-4: Compare bids in dictionary
best_bidder = None
highest_bid = 0

for key in bid_list:
    if bid_list[key] > highest_bid:
        best_bidder = key
        highest_bid = bid_list[key]

print(f"{best_bidder} won with the $ {highest_bid}.")