# Python 3.10 has a better solution in the match..case however the code below was running on Python 3.8.10

# Height and weight input
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Calculate BMI
bmi = weight / height ** 2

# Classify based on BMI (Note: BMI is rounded to nearest integer before displaying to user
#                              But the original BMI is used for classification)
if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese")
elif bmi > 35:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
