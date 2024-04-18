# Input a Python list of student heights
student_heights = [180, 124, 165, 173, 189, 169, 146]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
number_of_students = 0
for height in student_heights:
    total_height += height
    number_of_students += 1

average_height = round(total_height / number_of_students)

print(average_height)