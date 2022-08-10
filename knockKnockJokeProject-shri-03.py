'''
Program: Knock Knock Joke Project
Author: Shrikant Sharma
Description: This program writes a program that interacts with a user at the Python console to tell "knock-knock" jokes.
Filename: phloogsClass-shri-02.py
Purpose: Write a program that interacts with a user at the Python console to tell "knock-knock" jokes.
Revisions:
    00: announce and get the number of jokes the user wants to hear
    01: writes a function a program that interacts with a user at the Python console to tell "knock-knock" jokes.
    02: tell the knock-knock jokes as per user request
'''
# there are no literal constants
# there are no class definitions
import random  # importing random for shuffle function
# title of the program
print("Knock Knock Project")

def clean(s):  # function that returns the character without the below punctuations
    '''
    clean(s) returns the character in the string without below punctuations
    '''
    return ''.join([c for c in s if c not in "',.!?;\""])


used = []

# STEP 2:
# function that prompts takes the answer and returns the code with the jokes
def prompt_response(prompt, responses, suggest):
    '''
    prompt_response function that prompts takes the response and returns the code with the jokes
    '''
    print(prompt)
    response = input()
    response = clean(response).lower()
    if response in responses:
        p3 = random.randint(0, len(jokes)-1)
        while p3 in used:
            p3 = random.randint(0, len(jokes)-1)
        used.append(p3)
        p3 = jokes[p3]
        print(p3)
#STEP 3: tell the knock-knock jokes as per user request
        
        while True:  # using while loop to handle user based exception
            try:  # try catch to handle the same
                p4 = input()
                if p4 == p3.lower() + " who?" or p4 == p3 + " who?" or p4 == p3 + " who":
                    if p3 == "Cow says":  # knock knock jokes repository
                        print("No!  Cows say moo.  Owls say hoo! \n")
                        break  # break if valid
                    elif p3 == "Etch":
                        print("Please sneeze into your elbow! \n")
                        break  # break if valid
                    elif p3 == "Cash":
                        print("No thanks, I prefer peanuts. \n")
                        break  # break if valid
                    elif p3 == "Tank":
                        print("You’re welcome. \n")
                        break  # break if valid
                    elif p3 == "Ya":
                        print("Yahoo! I’m happy to see you too! \n")
                        break  # break if valid
                    elif p3 == "Boo":
                        print("Don't cry, it’s only a joke. \n")
                        break  # break if valid
                    elif p3 == "Dwayne":
                        print("Dwayne the tub before I dwown. \n")
                        break  # break if valid
                else:
                    print(f'The correct response is "{p3} who?"')
                    print('Try again\n')
            except:
                print("Provide correct input")
        else:
            print(f'The correct response is "{suggest}"')
            print('Try again\n')

# STEP 1: Announce, prompt, & get the number from the user
# announce
print("Ready to tell a knock-knock joke \n")
print("There are 7 available \n")
jokes = ["Cow says", "Etch", "Cash", "Tank", "Ya", "Boo", "Dwayne"]
while True:  # using while loop to handle user based exception
    # taking users input
    n = input("How many jokes would you like me to tell? ")
    if not n:
        break  # break if valid
    try:  # try catch to handle the same
        n = int(n)
        if n >= 1 and n <= 7:
            print("Ready to tell " + str(n) + " jokes! \n")
            for i in range(1, n+1):
                prompt_response('Knock-Knock',
                                ["whos there", "who is there",
                                 "who there", "who dere"],
                                "Who's there?")  # valid users feedback questions
            break  # break if valid
        else:
            # custom error message
            print("Enter a valid whole number from 1 to 7 \n")
    except Exception as e:  # define custom error
        print("Enter valid value")
