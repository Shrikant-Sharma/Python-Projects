'''
Program: Ultimate Language Translation with Python Lists using a Vocabulary File
Author: Shrikant Sharma
Description: This program translates words from English to French and vice versa
Filename: ultLangTran-shri-02.py
Purpose: Program to translate words from English to French and vice-versa

Revisions:
    00: Read a file and Store the data in a list
    01: Prompt the user for the word
    02: Translate the word into another language
    03: Print the translated word.
    04: If the word is not in the list, prompt the user to add it to the list
    05: Ask for what language the word in and prompt the user to enter the word
    06: Add the newly translated word to the dictionary.
    07: If the user doesn't want to add word to the list exit the program
    08: If user enters nothing then exit the program
    09: Store all the data in the existing file by overwriting it
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
# STEP 1: Announce, Prompt and Respond.
# Announce
print("Program to translate words from English to French and vice-versa")
# STEP 1: Read a file and Store the data in a list
with open('vocabulary.txt') as f:
    data = f.readlines()

data = [tuple(i.split()) for i in data if i != '\n']

english = []
french = []
for e, f in data:
    english.append(e)
    french.append(f)

while True:
    # STEP 2: Prompt the user for the word
    word = input('Enter an English or French word to translate: ').lower()
    # STEP 3: Translate the word into another language
    if word in english:
        ind = english.index(word)
        # STEP 4: Print the translated word
        print("The English word '{}' is '{}' in French".format(
            word, french[ind]))
    elif word in french:
        ind = french.index(word)
        # STEP 4: Print the translated word
        print("The French word '{}' is '{}' in English".format(
            word, english[ind]))
    # STEP 5: If the word is not in the list, prompt the user to add it to the list
    elif (word not in english) and (word not in french) and (word != ""):
        print("The word '{}' was not found in English or French word lists".format(word))
        add = input('Would you like to add '+word +
                    ' to the lists? <y>es or <n>o ').lower()
        if add == 'y' or add == 'yes':
            # STEP 6: Ask for what language the word in and prompt the user to enter the word
            lang = input('What language is '+word +
                         ' in? <E>nglish or <F>rench ').lower()
            if lang == 'e' or lang == 'english':
                # STEP 7: Add the newly translated word to the dictionary
                english.append(word)
                word2 = input('What is the French word for \'' +
                              word+'\'? ').lower()
                # STEP 7: Add the newly translated word to the dictionary
                french.append(word2)
            elif lang == 'f' or lang == 'french':
                french.append(word)
                word2 = input('What is the English word for ' +
                              word+'? ').lower()
                english.append(word2)
        # STEP 8: If the user doesn't want to add word to the list exit the program
        elif add == 'n' or add == 'no':
            break
    # STEP 8: If user enters nothing then exit the program
    elif word == '':
        break

# STEP 9: Store all the data in the existing file by overwriting it
data1 = list(zip(english, french))

with open('vocabulary.txt', 'w') as f:
    for english, french in data1:
        f.write(f'{english} {french}\n')
