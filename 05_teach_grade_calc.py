'''
Name: Garrett Helms
File: 05_teach_grade_calc.py
Date: May 22nd 2024

Purpose: grade calculation for school


'''

#ask user for grade input, convert to int
grade = int(input("What is your grade(%)?"))

#calculate letter grade according to int value of input, first part
'''if grade >= 90:
    print("Your grade is an A!")
elif grade >= 80:
    print("Your grade is a B.")
elif grade >= 70:
    print("Your grade is a C.")
elif grade >= 60:
    print("Your grade is a D. You failed!")
else:
    print("Your grade is an F! You failed!")'''

#calculate letter grade, second edition
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

#calculate the remainder to determine plus or minus
plus_minus_grade = grade % 10


#logic to determine correct output 
if grade >= 97:
    print(f"You're grade is {letter}+")
elif plus_minus_grade >= 7:
    print(f"You're grade is {letter}+")
elif plus_minus_grade < 3:
    print(f"You're grade is {letter}-")
elif 57 <= grade <= 59:
    print(f"You're grade is {letter}+")
elif grade <= 53:
    print(f"You're grade is {letter}-")



else:
    print(f"You're grade is {letter}")

#add whether its a passing or failing grade.
if grade >= 70:
    print("You passed!")
else:
    print("You failed!")

if grade >= 120:
    print(""" \n ...how the heck did you get so many points?
          You Einstein or something?""")


