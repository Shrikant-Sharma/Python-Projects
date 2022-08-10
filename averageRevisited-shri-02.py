'''
Program: Average Revisited
Author: Shrikant Sharma
Description: This program computes the average without knowing how many numbers to expect
Filename: averageRevisited-shri-02.py
Purpose: Compute the Average
Revisions:
    00: announce and get the numbers from the user
    01: compute the Average and print the result
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
# title of the program
print('Program to compute the average of the numbers provided.')
# STEP 1: Announce, prompt, & get response
# announce
inputs = list()
while (current := input("Enter a number: ")) != "":
    inputs.append(int(current))
print('You entered '+str(len(inputs))+' numbers')
# STEP 2: Compute the Average and echo back the result
print('The average is '+str(sum(inputs)/len(inputs)))
