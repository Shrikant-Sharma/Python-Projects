'''
Program: Phloogs Class
Author: Shrikant Sharma
Description: This program writes a function findGrade that takes a list of quiz grades and returns the average and a letter grade based on Dr. Phloog's criteria
Filename: phloogsClass-shri-02.py
Purpose: Write a function findGrade that takes a list of quiz grades and returns the average and a letter grade based on Dr. Phloog's criteria
Revisions:
    00: Write a function findGrade that takes a list of quiz grades and returns the average and a letter grade based on Dr. Phloog's criteria
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
def findGrade(grades):  # function that returns the average and a letter grade based on Dr. Phloog's criteria
    '''
    findGrade(grades) returns the average and a letter grade based on Dr. Phloog's criteria
    it takes a list of quiz grades
    '''
    # ENTER YOUR CODE HERE
    # it should compute the average grade after lowest
    # 1 out of 3 grades have been dropped and
    # a letter grade based on the average.
    # use the float variable "average" for the average
    # and the string variable "letter" for the grade
# STEP 1: Write a function findGrade that takes a list of quiz grades and returns the average and a letter grade based on Dr. Phloog's criteria
    grades.sort()
    if (len(grades) >= 3) and (len(grades) <= 5):
        i1 = grades[1:]
    elif (len(grades) >= 6) and (len(grades) <= 8):
        i1 = grades[2:]
    elif (len(grades) >= 9) and (len(grades) <= 10):
        i1 = grades[3:]
    average = sum(i1) / len(i1)
    if average < 80:
        letter = 'X'
    elif average > 90:
        letter = 'Z'
    else:
        letter = 'Y'
    return (average, letter)  # THIS RETURNS YOUR RESULTS
'''
DO NOT MODIFY ANY OF THE CODE BELOW
WHEN YOU RUN THE PROGRAM, YOUR RESULTS SHOULD BE ...
 80.00 --> Y 
 75.00 --> X 
 91.86 --> Z 
 79.86 --> X 
 85.17 --> Y 
'''
# title of the program
print('Program to calculate grades for Dr. Phloog\n')
# CODE TO TEST THE FUNCTION
grades = []
grades.append([50, 100, 60])  # [80.00,'Y']
grades.append([50, 100, 50, 50, 100, 50, 50, 100, 50])  # [75.00,'X']
grades.append([65, 100, 22, 89, 0, 100, 92, 78, 87, 97])  # [91.86,'Z']
grades.append([90, 70, 60, 100, 65, 95, 27, 55, 79, 60])  # [79.86,'X']
grades.append([65, 100, 22, 89, 45, 92, 78, 87])  # [85.17,'Y']
for item in grades:
    grade = findGrade(item)
    print(f"{grade[0]:6.2f} --> {grade[1]} ")
