'''
Program: List Comprehension Exercises
Author: Shrikant Sharma
Description: This program introduces the list comprehension in python
Filename: listComprExer-shri-03.py
Purpose: Comprehend the List,
Revisions:
    00: announce and provide the values to the variables x, y, z, and z1
    01: compute the comprehended list
    02: print the comprehended list which is stored in local variable
'''
# there are no import statements
# there are no class definitions
# title of the program
print('Program to print the comprehended list of the given literals definations.')
'''
    Simple List Comprehension & Sorting Template
    Complete the list comprehension exercises here
    Any functions you write must also have
    (1) a docstring that describes the input parameters
        and the value returned
    (2) at least two significant tests that verify the function
'''
# 1. List comprehension analysis
# Code


def linc(a, b=2):
    '''
    linc(a, b=2) function returns the calculated incremented values by 2 by default of the list element if the elements are integer.
    if the linc(a, 1) is called it will set the b's value to 1 and returns the incremented values by 1 of the list elements if the elements are integer.
    '''
    # PUT CODE HERE
    return [x+b for x in a if type(x) is int]


x = [1, 2, '3', 4]
y = linc(x)  # [3,4,6]
z = linc(x, 1)  # [2,3,5]
print(x)
print(y)
print(z)

# 2. the listInc() function


def listInc(a):
    '''
    listInc(a) function returns the calculated incremented values by 1 of the list element if the elements are integer.
    '''
    # YOUR CODE HERE
    return [x+1 for x in a if type(x) is int]


    # listInc() tests
assert listInc([7, 2, 4, 8]) == [8, 3, 5, 9], 'listInc failed [7,2,4,8]'
assert listInc([9, -1, 0.0, 5]) == [10, 0, 6], 'listInc failed [9,-1,0.0,5]'
print('listInc is OK\n')
# 3. the listOut() function


def listOut(a):
    '''
    listOut(a) function returns the each element of the list in a new line.
    '''
    # YOUR CODE HERE
    return '\n'.join([str(i) for i in a])

    # listOut() tests
print(listOut([7, 2, 'OK', 8]))
print(listOut([[1, 2], 2.0, '$', 8]))
# 4. statements that move items between lists
# end of A to beginning of B
a, b = [1, 2, 3], [4, 5, 6]
# YOUR CODE HERE
a = [i if i != a[-1] else b.insert(0, i) for i in a]
print(a, b)
# beginning of A to end of B
a, b = [1, 2, 3], [4, 5, 6]
# YOUR CODE HERE
a = a = [b.append(i) if i == a[0] else i for i in a]
print(a, b, '\n')
# 5a. the rotateForward() function


def rotateForward(a):
    '''
    rotateForward(a) function returns the list's last element moving forward(0th index) of the list.
    '''
    # YOUR CODE HERE
    return [a[i-1] for i in range(len(a))]

    # rotateForward() tests
assert rotateForward([1, 2, 3, 4]) == [4, 1, 2, 3], 'rotateForward failed'
print('rotateForward ok\n')
# 5a. the rotateForward() function


def rotateBackward(a):
    '''
    rotateForward(a) function returns the list's first element moving backward(last index) of the list.
    '''
    # YOUR CODE HERE
    return [a[(i+1) % len(a)] for i in range(len(a))]

    # rotateForward() tests
assert rotateBackward([1, 2, 3, 4]) == [2, 3, 4, 1, ], 'rotateBackward failed'
print('rotateBackward ok\n')

# 6. Analysis of iSort()


def iSort(x, n=2):
    '''
    iSort(x, n=2) function returns the sorted order of the 2nd index in alphabetical order of the list elements.
    if iSort(x, 1) function is called it will set the n's value to 1 and returns the sorted order of the 1st index in alphabetical order of the list elements.
    '''
    # PUT CODE HERE
    return sorted(x, key=lambda x: x[n])


x = [(1, 'one', 'uno'), (2, 'two', 'dos'), (3, 'three', 'tres')]
print(iSort(x))
print(iSort(x, 1))
print()
# 7. Length sorting
z = ['bzz', 'z', 'cz', 'azzz']
# YOUR CODE HERE
z1 = sorted(z, key=len)
print(z1, '\n')
# 8. the backSort() function


def backSort(a):
    '''
    backSort(a) function returns the list's last index in the elements in the alphabetical order.
    '''
    # YOUR CODE HERE
    return sorted(a, key=lambda a: a[-1])

    # backSort() tests
assert backSort(['red', 'yellow', 'blue', 'green', 'black']) == \
    ['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
print('backSort OK')
