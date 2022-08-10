'''
Program: Scramble Challenge
Author: Shrikant Sharma
Description: This program introduces the scramble challenge in python
Filename: scramChall-shri-02.py
Purpose: print the scramble word from given list
Revisions:
    00: Sort the tuples based on the integer value in each.  Use a lambda construct to provide the sort key.
    01: Use a list comprehension to create a list of characters for each word.
    02: Use the join() method to create a string for each of the four words and print them.
'''
# there are no import statements
# there are no class definitions
# there are no function definitions
# title of the program
print('Program to print the scrambled word from the given list.')
'''
    Scrambled Words
    The source code below defines four encoded common English words.
    Each word is 7 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions in your solution.
'''
z = [('v', 'c', 'l', 6, 'r'), ('i', 'a', 'i', 4, 't'),
     ('a', 'f', 'g', 1, 'p'), ('h', 'n', 'r', 3, 's'),
     ('e', 'e', 'a', 7, 'e'), ('c', 'i', 'o', 2, 'a'),
     ('e', 'n', 'l', 5, 'u')]
# Step 1:   Sort the tuples based on the integer value in each.  Use a
#           lambda construct to provide the sort key.
z.sort(key=lambda a: a[3])

# Step 2:   Use a list comprehension to create a list of characters
#           for each word.
l1 = list([a[0] for a in z])
l2 = list([a[1] for a in z])
l3 = list([a[2] for a in z])
l4 = list([a[4] for a in z])

# Step 3:   Use the join() method to create a string for each of the
#           four words and print them.
s1 = ''.join(l1)
s2 = ''.join(l2)
s3 = ''.join(l3)
s4 = ''.join(l4)
print(s1)
print(s2)
print(s3)
print(s4)
