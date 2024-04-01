print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# criar a variavel score
score_true = 0
score_love = 0
total_score = 0

names = (name1 + name2).lower()
names_chars = list(names)

for char in names_chars:
  if char == 't' or char == 'r' or char == 'u' or char == 'e':
    score_true += 1
  if char == 'l' or char == 'o' or char == 'v' or char == 'e':
    score_love += 1

str_score = str(score_true) + str(score_love)
final_score = int(str_score)

if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")

# or another way
# combined_names = name1 + name2
# lower_names = combined_names.lower()

# t = lower_names.count('t')
# r = lower_names.count('r')
# u = lower_names.count('u')
# e = lower_names.count('e')

# first_digit = t + r + u + e

# l = lower_names.count('l')
# o = lower_names.count('o')
# v = lower_names.count('v')
# e = lower_names.count('e')

# second_digit = l + o + v + e

# score = str(first_digit) + str(second_digit)

# if (int(score) < 10) or (int(score) > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (int(score) > 40) and (int(score) < 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")


