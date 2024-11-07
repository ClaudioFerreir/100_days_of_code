from random import randint

from game_data import data

# Generate a random number into the game data index
def take_item():
    index = randint(0, len(data)-1)
    return data[index]

print(take_item())