'''
Program: Linear Prediction Sequence
Author: Shrikant Sharma
Description: This program computes the Linear Prediction Sequence
Filename: linearPrediction-shri-03.py
Purpose: Compute the Linear Prediction Sequence
Revisions:
    00: announce and get the 1st and 2nd number from the user
    01: compute the Linear Prediction Sequence
    02: print the result
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
### STEP 1: Ammounce, prompt, & get response
# announce
print('Compute the Linear Prediction Sequence\n')
# prompt user and get a response in string
a = (input('Enter the 1st number: '))
b = (input('Enter the 2nd number: '))
# converting the string into required data type
a = int(a)
b = int(b)
### STEP 2: Compute the Linear Prediction Sequence
if a < b:
    diff = b - a
    c = b + diff
    # echo back the 1st, 2nd number and the next Sequence
    print('The Linear Sequence is: ',a,' ',b,' ',c)
elif a > b:
    diff = a - b
    c = b - diff
    # echo back the 1st, 2nd number and the next Sequence
    print('The Linear Sequence is: ',a,' ',b,' ',c)
elif a == b:
    print('Invalid Sequence')