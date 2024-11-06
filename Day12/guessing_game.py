import random

from art import logo

def game():

    print(logo)
    number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        attempts = 0
        print("That's not a valid option. Refresh the page to run again!")

    def guess_again(n):
        if n != 1:
            print("Guess again.")

    # Here starts the looping
    for i in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            return
        elif guess > number and attempts > 1:
            print("Too high.")
            guess_again(attempts)
        else:
            if attempts > 1:
                print("Too low.")
                guess_again(attempts)

        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again!!!")
            print(f"The number was {number}.")
            return


game()