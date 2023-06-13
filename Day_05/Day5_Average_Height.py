# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total_height = 0

for each_height in student_heights:
    total_height += each_height

number_of_students = 0

for student in student_heights:
    number_of_students += 1
print(number_of_students)

result = total_height / number_of_students
rounded_result = round(result,)
print(rounded_result)