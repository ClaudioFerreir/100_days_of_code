print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# criar a variavel score
score_true = 0
score_love = 0
total_score = 0

names = (name1 + name2).upper()
names_chars = list(names)

for char in names_chars:
  if char == 'T' or char == 'R' or char == 'U' or char == 'E':
    score_true += 1
  if char == 'L' or char == 'O' or char == 'V' or char == 'E':
    score_love += 1

str_score = str(score_true) + str(score_love)
final_score = int(str_score)

if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")
