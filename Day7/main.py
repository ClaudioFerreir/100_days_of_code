import random
from game_words import word_list
from game_pics import stages, logo

# TODO 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#while True:
#    guess = input("Please enter a single letter: ").lower()
#    # Verifica se é uma unica letra
#    if len(guess) == 1 and guess.isalpha():
#        print(f"You entered the letter: {guess}")
#        break
#    else:
#        print("Error: Please enter only a single letter.")
# TODO 3 - Check if the letter the user guessed (guess) is one of the letters in the chose_word. Print "Right"if it is, "Wrong" if it's not.
#for letter in chosen_word:
#    if letter == guess:
#        print("Right")
#    else:
#        print("Wrong")

# TODO 4 - Create a empty String called placeholder
# TODO 5 - For each letter in the chosen_word add a _ to placeholder.
# TODO 6 - So it the chosen_word was "apple". placeholder should be _____ with 5 "_" representing each letter to guess.
placeholder = list("_" * len(chosen_word))

# TODO 7 - Add a letter guessed in the string placeholder
#for index, value in enumerate(chosen_word):
#    if value == guess:
#        placeholder[index] = value

#print(placeholder)

# TODO 8 - User a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word.
# TODO 9 - At that point display has no more blanks ("_"). Then you can tell they've won.

spaces = len(chosen_word)
# TODO 10 - Create a variable called lives to keep track of the number of lives left. Set lives to equal 6.
lives = 6
chosen_letters = []

while spaces > 0:
    print(f"**************************************** {lives} LIVES LEFT *****************************************")
    guess = input("Please enter a single letter: ").lower()
    # Verifica se é uma unica letra
    if len(guess) == 1 and guess.isalpha():
        print(f"You entered the letter: {guess}")
        if guess not in chosen_letters:
            chosen_letters.append(guess)
            if guess in chosen_word:
                for index, value in enumerate(chosen_word):
                    if value == guess:
                        placeholder[index] = value
                spaces = placeholder.count("_")
                if spaces == 0:
                    print(f"**************************************** YOU WON!!! *********************************************")
            # TODO 11 - If guess is not a letter in the chosen_word. Then reduce lives by 1.
            else:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
        else:
            print("You have already guessed that letter.")
    else:
        print("Error: Please enter only a single letter alphabetically.")
    print(stages[lives])
    print(placeholder)
    # TODO 12 - If lives goes down to 0 then the game should end, and it should print "You lose."
    if lives == 0:
        print(f"*********************************** IT WAS '{chosen_word}'! YOU LOSE!!! *********************************************")
        break




