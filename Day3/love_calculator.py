print("The Love Calculator is calculating your score...")
name1 = "Ashton Kutcher	" # What is your name?
name2 = "Mila Kunis" # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# criar a variavel score
score_true = 0
score_love = 0
total_score = 0
# somar as duas strings
# transformar as letras em maiusculas
# separar as letras na string
names = (name1 + name2).upper()
names_chars = list(names)
# fazer a pontuação
for char in names_chars:
# comparar as letras com TRUE
  if char == 'T' or char == 'R' or char == 'U' or char == 'E':
    score_true += 1
# comparar as letras com LOVE
  if char == 'L' or char == 'O' or char == 'V' or char == 'E':
    score_love += 1
# fazer a pontuação
print(score_true)
print(score_love)
# conferir o total do score 
str_score = str(score_true) + str(score_love)
# printar o resultado
final_score = int(str_score)
print(f"Your score is {final_score}.")