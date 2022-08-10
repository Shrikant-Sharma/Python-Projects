'''
Program: Simple Average
Author: Shrikant Sharma
Description: This program calculate the Average of a sequence of numbers
Filename: simpleAverage-shri-02.py
Purpose: Calculate the Average of a Sequence of Numbers
Revisions:
    00: announce and get the sequence from the user
    01: compute the simple average
    02: print the result
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
# STEP 1: Announce, prompt, & get response
# declare the sum variable
sum = 0
# announce
num = int(input("How many numbers would you like to average? "))
# STEP 2: Compute the Simple Average
for i in range(1, num+1):
    simave = int(input("Enter number " + str(i) + ": "))
    sum = sum + simave
avg = sum / num
# echo back the simple average
print("The average is " + str(avg))
