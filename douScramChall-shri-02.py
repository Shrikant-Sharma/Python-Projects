'''
Program: Double Scramble Challenge
Author: Shrikant Sharma
Description: This program introduces the double scramble challenge in python
Filename: douScramChall-shri-02.py
Purpose: print the double scramble word from given list
Revisions:
    00: Rotate each list in z so the integer is in the zero position without changing the order of the characters.
    01: Sort the lists based on the integer value in each.
    02: Use a list comprehension to create a list of characters for each word.
    03: Use the join() method to create a string for each of the four words and print them.
'''
# there are no import statements
# there are no class definitions
# there are no function definitions
# title of the program
print('Program to print the double scrambled word from the given list.')

'''
    Double Scrambled Words
    The variable z contains four encoded common English words.
    Each word is 5 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions where possible.
    *** Note that unlike the previous problem, each item in z is a list.
        Each list has an integer that encodes the position in a different
        location in the list.  The characters are in the correct order but
        you will need to rotate each list so the integers are in the same
        location in each list.  The most convenient location would be at
        index zero because then, you would not need to provide a sort key.
    Example: rotate z[0] so it looks like this: [3, 't', 'n','s', 'a']
'''

z = [['s', 'a', 3, 't', 'n'], ['h', 'b', 'c', 1, 'p'],
     ['h', 'y', 'c', 'k', 5], [4, 'c', 'e', 'i', 'l'],
     ['o', 'a', 'h', 2, 'i']]

# Step 1:   Rotate each list in z so the integer is in the zero position
#           without changing the order of the characters.
z1 = [z[0][i-3] for i in range(len(z[0]))]
z2 = [z[1][i-2] for i in range(len(z[1]))]
z3 = [z[2][i-1] for i in range(len(z[2]))]
z4 = [z[4][i-2] for i in range(len(z[4]))]
z = list([z1, z2, z3, z[3], z4])

# Step 2:   Sort the lists based on the integer value in each.
z.sort(key=lambda a: a[0])

# Step 3:   Use a list comprehension to create a list of characters
#           for each word.
l1 = list([a[1] for a in z])
l2 = list([a[2] for a in z])
l3 = list([a[3] for a in z])
l4 = list([a[4] for a in z])

# Step 4:   Use the join() method to create a string for each of the
#           four words and print them.
s1 = ''.join(l1)
s2 = ''.join(l2)
s3 = ''.join(l3)
s4 = ''.join(l4)
print(s1)
print(s2)
print(s3)
print(s4)
