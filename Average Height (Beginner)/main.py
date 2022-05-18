# Note it is advised not to use len() and sum() functions to prioritize learning new concepts

# Take heights as input, Eg. 180 176 159 188
student_heights = input("Input a list of student heights ").split()

# Looping across the list to cast values into integers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
num_student = 0

# For loop to calculate total heights and count number of students in list
for height in student_heights:
    total_height += height
    num_student += 1

# calculating and printing average height
avg_height = total_height/num_student
print(str(round(avg_height)))
