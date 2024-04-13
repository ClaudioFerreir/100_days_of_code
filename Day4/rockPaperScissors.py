import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
computer_choice = random.randint(0, 2)

print(images[your_choice])