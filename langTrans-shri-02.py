'''
Program: Language Translation by Dictionaries
Author: Shrikant Sharma
Description: This program translates words from English to French, Spanish, and German and vice versa
Filename: langTrans-shri-02.py
Purpose: Program to translate words from English to French, Spanish, and German and vice-versa

Revisions:
    00: Prompt the user for the word
    01: Translate the word into another language
    02: Display the available languages
    03: Select the language
    04: Display the word in translated language
'''
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
# STEP 1: Announce, Prompt and Respond.
# Announce
print("Language Translator")
colors = {}
colors['red'] = {}
colors['red'].update({'french': 'rouge'})
colors['red'].update({'spanish': 'rojo'})
colors['red'].update({'german': 'rot'})
colors['green'] = {}
colors['green'].update({'french': 'vert'})
colors['green'].update({'spanish': 'verde'})
colors['green'].update({'german': 'grun'})
colors['yellow'] = {}
colors['yellow'].update({'french': 'jaune'})
colors['yellow'].update({'spanish': 'amarillo'})
colors['yellow'].update({'german': 'gelb'})
colors['blue'] = {}
colors['blue'].update({'french': 'bleu'})
colors['blue'].update({'spanish': 'azul'})
colors['blue'].update({'german': 'blau'})
print("Available English words are: ", end="")
for color in colors:
    print(color+"; ", end="")
print()
# STEP 1: Prompt the user for the word
color_in_english = input("Please enter a color in English: ").lower()
# STEP 2: Display the available languages
print("Available language translations are: ", end='')
for k in colors[color_in_english]:
    print(k+"; ", end='')
print()
# STEP 3: Select the language
lang = input("Please enter a language from the list: ").lower()
print()
# STEP 4: Display the word in translated language
print("The word \""+color_in_english+"\" in "
      + lang.capitalize()+" is \""+colors[color_in_english][lang]+"\".")
