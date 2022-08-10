'''
Program: Letter Grades
Author: Shrikant Sharma
Description: This program computes the Letter Grade
Filename: letterGrades-shri-03.py
Purpose: Compute the Letter Grade
Revisions:
    00: announce and get the score from the user
    01: compute the Letter Grade
    02: print the result
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
### STEP 1: Ammounce, prompt, & get response
# announce
print('Compute the Letter Grades\n')
score = float(input("Please enter the score: "))
### STEP 2: Compute the Letter Grade
# define letterGrade function and compute the letter grade
def letterGrade(score):
    if score >= 95.0:
        return "A+"
    elif score >= 90.0 and score < 95.0:
        return "A"
    elif score >= 85.0 and score < 90.0:
        return "A-"
    elif score >= 80.0 and score < 85.0:
        return "B+"
    elif score >= 75.0 and score < 80.0:
        return "B"
    elif score >= 70.0 and score < 75.0:
        return "B-"
    elif score >= 65.0 and score < 70.0:
        return "C+"
    elif score >= 60.0 and score < 65.0:
        return "C"
    elif score >= 55.0 and score < 60.0:
        return "C-"
    else:
        return "F"
    # echo back the letter grade
print('The letter grade for ', score, ' percent is ', letterGrade(score), '.')

