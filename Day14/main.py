from random import randint

from game_data import data
from art import logo, vs


def take_item():
    """Refer a item into the game_data"""
    index = randint(0, len(data) - 1)
    item = data[index]
    return item

def game():
    item_a = take_item()
    item_b = take_item()
    score = 0

    next_round = True

    while next_round:
        print(logo)

        if score != 0:
            print(f"You're right! Current score: {score}.")

        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}.")
        print(vs)
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}.")

        option = input("Who has more followers? Type 'A' or 'B': ").upper()

        if option == 'A' and item_a['follower_count'] > item_b['follower_count']:
            item_b = take_item()
            score += 1

        elif option == 'B' and item_b['follower_count'] > item_a['follower_count']:
            item_a = item_b
            item_b = take_item()
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}!")
            next_round = False

game()