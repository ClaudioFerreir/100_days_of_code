target = 52 # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum_even_numbers = 0
for number in range(1, target+1):
  if number % 2 == 0:
    sum_even_numbers += number

print(sum_even_numbers)