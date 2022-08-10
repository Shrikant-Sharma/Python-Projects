'''
Program: Circumference of a Circle
Author: Shrikant Sharma
Description: This program computes the Circumference of a Circle
Filename: circumCircle-shri-02.py
Purpose: Compute the Circumference of a Circle
Revisions:
    00: announce and get the diameter from the user
    01: compute the circumference of a circle
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
### STEP 1: Ammounce, prompt, & get response
# announce
print('Compute the Circumference of a Circle\n')
# prompt user and get a response in string
d = (input('Enter the diameter of a circle '))
# converting the string into required data type 
d = float(d)
### STEP 2: Compute the Circumference of a Circle
c = d * 3.14
# echo back the Diameter and Circumference of a Circle
print('The circumference of a circle of diameter ',d,' is ',c)
