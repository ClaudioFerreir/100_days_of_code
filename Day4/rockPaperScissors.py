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

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
computer_choice = random.randint(0, 2)

print(images[your_choice])

print('Computer choise: ')
print(images[computer_choice])

if (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice == 1):
    print('you win')
elif your_choice == computer_choice:
    print ('you draw')
else:
    print('you lose')
    