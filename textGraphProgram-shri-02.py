'''
Program: Text Graph Program
Author: Shrikant Sharma
Description: This program draws the Text Graph for entered positive whole numbers
Filename: textGraphProgram-shri-02.py
Purpose: Displays the Text Graph
Revisions:
    00: announce and get the postitive whole numbers from the user
    01: compute and displays the Text Graph
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
# STEP 1: Ammounce, prompt, & get response
# announce
num = input("Enter up to 10 positive whole numbers less than 50: ")
# STEP 2: Compute and Display the Text Graph
# compute and display the text graph
numbers = num.split()
for n in numbers:
    if n.isnumeric():
        n1 = int(n)
        if n1 < 50:
            print("="*int(n1))
        elif n1 > 50:
            print("?")
    else:
        print("?")
