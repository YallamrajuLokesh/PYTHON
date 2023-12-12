loki=["lol","heloo","lmao"]
for i in loki:
  print(i)
  '''lol
heloo
lmao
'''
   print(i+" loki")
'''output-
lol loki
heloo loki
lmao loki
'''
#exercise solving 
#question
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
#solution
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

for i in range(1,11,2): #(starting point,ending point,step)



#adding even numbers
arget = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum=0
for i in range(1,target+1):
 if i%2==0:
   sum += i
print(sum)
