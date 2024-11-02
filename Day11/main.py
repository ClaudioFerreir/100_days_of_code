import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#start = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ").lower()

# Initial cards
player_cards = random.choices(cards, k=2)
# print(player_cards)

player_points = 0

# Player's turn
for card in player_cards:
    player_points += card
print(f"the player has {player_points} points")

# Computer_points
computer_points = random.choice(cards)

# Computer's round
def computer_round(points, player):
    new_card = random.choice(cards)
    total_points = points + new_card
    print(total_points)
    if total_points > 21:
        print("You Win!!!")
    elif total_points > player:
        print("You Lose!!!")
    elif total_points == player:
        print("You Draw!!!")
    else:
        computer_round(total_points, player)
    return total_points

# player round
def player_round(points):
    if points == 21:
        print("You Win!!!")
    elif points > 21:
        print("You Lose!!!")
    else:
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if should_continue == 'y':
            new_card = random.choice(cards)
            print(new_card)
            points += new_card
            print(points)
            player_round(points)
        elif should_continue == 'n':
            computer_round(computer_points, points)
    return points
#
player_round(player_points)




# computer_cards = random.choices(cards, k=2)
#
# print(your_cards, computer_cards[0])