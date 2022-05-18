# Taking list of scores as input, Eg. 67 85 91 45 99
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Assigning first element in the list as the highest score by default
highest_score = student_scores[0]

# Looping through elements 1 through n (not 0) to find the new highest score (if exists)
# Note: max() function is not used to learn more about loops
for score in range(1, len(student_scores)):
    if student_scores[score] > highest_score:
        highest_score = student_scores[score]

print(f"The highest score in the class is: {highest_score}")
