import random
import os

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ").lower()

while start == 'y':

    print("\n" * 15)
    print(art.logo)

    # Player initial cards
    player_cards = random.choices(cards, k=2)
    # Player's points
    player_points = sum(player_cards)

    # Computer initial cards
    computer_cards = [random.choice(cards)]
    # Computer's points
    computer_points = computer_cards[0]

    # Final computer's turn message
    def final_computer_round(player_f_hand, player_f_score, computer_f_hand, computer_f_score):
        print(f"Your final hand: {player_f_hand}, final score: {player_f_score}")
        print(f"Computer's final hand: {computer_f_hand}, final score: {computer_f_score}")

    # Computer's turn
    def computer_round(points, player, player_hand):
        computer_hand = [points]
        new_card = random.choice(cards)
        computer_hand.append(new_card)
        total_points = points + new_card

        if total_points > 21:
            final_computer_round(player_hand, player, computer_hand, total_points)
            print("Opponent went over. You win!!!")
        elif total_points == 21:
            final_computer_round(player_hand, player, computer_hand, total_points)
            print("Lose, opponent has Blackjack!!!")
        elif total_points > player:
            final_computer_round(player_hand, player, computer_hand, total_points)
            print("You Lose!!!")
        elif total_points == player:
            final_computer_round(player_hand, player, computer_hand, total_points)
            print("Draw!!!")
        else:
            computer_round(total_points, player, player_cards)


    # player's turn
    def player_round(points):

        print(f"Your cards: {player_cards}, current score: {points}")
        print(f"Computer's first card: {computer_points}")

        if points == 21:
            print("You Win!!!")
        elif points > 21:
            print("You went over. You lose!")
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                new_card = random.choice(cards)
                points += new_card
                player_cards.append(new_card)
                player_round(points)
            elif should_continue == 'n':
                computer_round(computer_points, points, player_cards)

    player_round(player_points)

    start = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ").lower()



