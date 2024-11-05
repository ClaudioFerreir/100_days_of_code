import random

def game():
    number = random.randint(1, 100)
    print(number)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    # Here starts the looping
    print(f"You have {attempts} attempts to guess the number.")

    guess = int(input("Make a guess: "))

    if guess == number:
        print("You are correct!")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")


game()