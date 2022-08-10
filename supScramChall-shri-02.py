'''
Program: Super Scramble Challenge
Author: Shrikant Sharma
Description: This program introduces the super scramble challenge in python
Filename: superScramChall-shri-02.py
Purpose: print the super scramble word from given list
Revisions:
    00: PUT YOUR ROTATE FUNCTION HERE
    01: ALIGN: DO STEP (1) IN A LOOP HERE
    02: SORT & BUILD: DO THE REST OF THE STEPS IN A LOOP HERE.
'''
# there are no import statements
# there are no class definitions
# title of the program
print('Program to print the super scrambled word from the given list.')
'''
Super Scramble Challenge
Consider this list of lists that encodes
three 3-letter words ...
    [['a','p','r', 2 ],
     ['n','i', 3 ,'t'],
     ['a', 1 ,'c','e']]
To unscramble this mess, you must ...
(1) align: rotate each item in the list so the integer
    is in location 0 ...
    [[ 2 ,'a','p','r'],
     [ 3 ,'t','n','i'],
     [ 1 ,'c','e','a']]
(2) sort: sort the lists based on the integer ...
    [[ 1 ,'c','e','a'],
     [ 2 ,'a','p','r'],
     [ 3 ,'t','n','i']]
(3) build: assemble the first word from
    the second item in each list (cat)
(4) sort: sort the lists based on the first word ...
    [[ 2 ,'a','p','r'],
     [ 1 ,'c','e','a'],
     [ 3 ,'t','n','i']]
(5) build: assemble the second word (pen)
(6) sort: sort by the second word
(7) build: assemble the third word (air)
===========================================
Now, check out the mess below and write
Python statements to discover six 7-letter words
*** DO NOT HARD-CODE A SOLUTION ***
HINTS
(1) To rotate, pop and then insert at 0.
    Repeat until the int is in the correct location
    I recommend a writing a function for this
(2) enumerate() will be helpful in copying the
    rotated item back to the data structure
    It will provide the index of the current item
(3) a lambda expression will be helpful in establishing
    a sort key
(4) ''.join() along with a list comprehension
    will be helpful in assembling the words
(5) it is possible to do this in 7 lines of code
    Does not include the rotate function (one additional line)
    your results may vary
(6) a lambda function can be assigned to a variable and used
    as if it were defined using def
'''
mess = [['o', 'c', 'h', 'c', 'a', 64, 'd'],
        ['o', 'o', 91, 'y', 'y', 'e', 'i'],
        ['u', 'r', 'o', 'u', 'y', 46, 'e'],
        ['u', 'y', 'e', 'r', 19, 't', 't'],
        ['a', 'h', 55, 's', 'n', 'i', 's'],
        [27, 'u', 'r', 't', 'r', 'r', 'n'],
        [72, 'a', 'c', 'p', 't', 'g', 'm']]

# PUT YOUR ROTATE FUNCTION HERE
eList = []


def rotate_element(ele):
    '''
    rotate_element(ele) function returns the list of elements until the 1st element is not integer.
    '''
    for i in ele:
        if type(i) is int:
            return [ele[(j-(len(ele)-ele.index(i))) % len(ele)] for j, k in enumerate(item)]


# ALIGN: DO STEP (1) IN A LOOP HERE
for item in mess:
    eList.append(rotate_element(item)) #rotate the sublist to get the first element as integer
# SORT & BUILD: DO THE REST OF THE STEPS IN A LOOP HERE
for y in range(0, len(eList) - 1):
    eList.sort(key=lambda a: a[y]) #sorts the list according to the integer value
    print(''.join([a[y+1] for a in eList])) #creates the string by the joining the sublist and prints them

