'''
Program: Guessing Game
Author: Shrikant Sharma
Description: This program guesses a number within a specific range in the fewest number of guesses.
Filename: guessingGame-shri-02.py
Purpose: Guess a number within a certain range in the fewest number of guesses
Revisions:
    00: announce and get the number from the user
    01: guess the number within a specific range in the fewest number of guesses and print the result
'''
# there are no literal constants
# there are no class definitions
# there are no function definitions
import math  # import math
import random  # import random
# title of the program
print("Guess the Secret Number")
print()
# STEP 1: Announce, prompt, & get the number from the user
# announce
nMax = int(input("Enter the maximum number in the range: "))
# STEP 2: Guess the number within specific range and print the result
nGuesses = int(math.log2(nMax)+1)  # number of guesses
secret_number = random.randrange(1, nMax)
print()
print("Try to guess a secret number from 1 to ", nMax, " (inclusive).")
print()
for i in range(1, nGuesses+1):
    if nGuesses > 1:
        print("You have ", nGuesses, " guesses available.")
        n = int(input("Enter your guess: "))
        if n < secret_number:
            print("The secret number is greater than {}.".format(n))
        elif n > secret_number:
            print("The secret number is less than {}.".format(n))
        else:
            print("Correct. Well done!")
            break
    elif nGuesses == 1:
        print("You have ", nGuesses, " guess available.")
        n = int(input("Enter your guess: "))
        if n == secret_number:
            print("Correct. Well done!")
            break
        else:
            print()
            print("Sorry. No more guesses are allowed.")
            print("The secret number was ", secret_number)
    nGuesses = nGuesses - 1
