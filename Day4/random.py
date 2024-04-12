import random

random_integer = random.randint(1, 10)
print(random_integer)

# generates a float between 0 and 1, but not includes 1  (0.0000000 - 0.9999999)
random_float = random.random() 
print(random_float)

# how to create a number between 0 and 5
random_float_between_0_and_5 = random_float * 5
print(random_float_between_0_and_5)

# random uses
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")