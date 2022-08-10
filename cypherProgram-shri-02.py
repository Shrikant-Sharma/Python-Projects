'''
Program: Cypher Program
Author: Shrikant Sharma
Description: This program computes the Cypher code for the given word
Filename: cypherProgram-shri-02.py
Purpose: Compute the Cypher Code
Revisions:
    00: announce and get the score from the user
    01: compute the Cypher code
    02: print the result
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
# STEP 1: Ammounce, prompt, & get response
# announce
conv = ''
score = input("Enter a word: ")
# STEP 2: Compute the Cypher code
# define the given word in lower case and compute the cypher code
score = score.lower()
for e in score:
    conv = conv + str(ord(e) - 97) + ' '
# echo back the cypher code
print("The code for "+score+" is: "+conv.strip())
