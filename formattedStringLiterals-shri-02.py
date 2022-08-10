'''
Program: Formatted String Literals
Author: Shrikant Sharma
Description: This program introduces the formatted string functionality in python
Filename: formattedStringLiterals-shri-02.py
Purpose: Format the String Literals
Revisions:
    00: announce and provide the values to the variables x, y, and z
    01: compute the formatted string in local variable
    02: print the formatted string which is stored in local variable
'''
# there are no import statements
# there are no class definitions
# there are no function definitions
# title of the program
print('Program to print the formatted string of the given literals definations.')
# f-string exercises
# STEP 1: Announce and provide the values to the variables x, y, and z
# announce
# x, y, z variables for the exercise
x = 27
y = 3.14159
z = 'pi'
# build f-strings to each specification below
# 10 different exercises of increasing complexity
# STEP 2: Compute the formatted string in local variable
''' #1
Create a string variable s that uses
variable x to create this string ...
"27 is a whole number"
'''
# edit the assignment statement below
s = f'{x} is a whole number'
# print and echo back the formatted string which is stored in local variable
print(f"#1 ...\n{s}")

# STEP 2: Compute the formatted string in local variable
''' #2
Create a string variable s that uses variable x
and the type() function to create this string ...
"27 is <class 'int'>"
'''
# edit the assignment statement below
s = f'{x} is {type(x)}'
# print and echo back the formatted string which is stored in local variable
print(f"#2 ...\n{s}")

# STEP 2: Compute the formatted string in local variable
''' #3
Create a string variable q that uses
variable y to create this string ...
"pi to 6 digits is 3.14159"
'''
# edit the assignment statement below
q = f'{z} to 6 digits is {y}'
# print and echo back the formatted string which is stored in local variable
print(f"#3 ...\n{q}")

# STEP 2: Compute the formatted string in local variable
''' #4
Create a string variable q that uses
variable y to create this string ...
"pi to 3 digits is 3.14"
'''
# edit the assignment statement below
q = f'{z} to 3 digits is {y:1.2f}'
# print and echo back the formatted string which is stored in local variable
print(f"#4 ...\n{q}")

# STEP 2: Compute the formatted string in local variable
''' #5
Create a string variable r that uses
variables y and z to create this string ...
"pi to 4 digits is 3.14"
'''
# edit the assignment statement below
r = f'{z} to 4 digits is {y:.3f}'
# print and echo back the formatted string which is stored in local variable
print(f"#5 ...\n{r}")

# STEP 2: Compute the formatted string in local variable
''' #6
Create a string variable r that uses variables x,
y, and z to create this output ...
"    27     3.14159      pi    "
Each variable is centered across 10 spaces
'''
# edit the assignment statement below
r = f'{x:^10}{y:^10}{z:^10}'
# print and echo back the formatted string which is stored in local variable
print(f"#6 ...\n{r}")

# STEP 2: Compute the formatted string in local variable
''' #7
Create a string variable r that uses variables x,
y, and z to create this table ...
"    x         y         z     
     27     3.14159      pi   "
Each item is centered across 10 spaces.
Use the newline escape sequence as needed.
'''
# edit the assignment statement below
r = f'{"x":^10}{"y":^10}{"z":^10}\n{x:^10}{y:^10}{z:^10}'
# print and echo back the formatted string which is stored in local variable
print(f"#7 ...\n{r}")

# STEP 2: Compute the formatted string in local variable
''' #8
Create a string variable q that uses variables x and
y as US currency (two decimal places, preceded
by a dollar sign, left justified across 10 spaces ...
"$27.00    $3.14     "
'''
# edit the assignment statement below
q = f'${f"{x:.2f}":<10}${f"{y:.2f}":<10}'
# print and echo back the formatted string which is stored in local variable
print(f"#8 ...\n{q}")

# STEP 2: Compute the formatted string in local variable
''' #9
Create a string variable q that uses variables x and
y as US currency (two decimal places, preceded
by a dollar sign, center justified across 10 spaces ...
"  $27.00    $3.14   "
'''
# edit the assignment statement below
q = f'{f"${x:.2f}":^10}{f"${y:.2f}":^10}'
# print and echo back the formatted string which is stored in local variable
print(f"#9 ...\n{q}")

# STEP 2: Compute the formatted string in local variable
''' #10
Create a string variable s that uses variables x and
y as US currency (two decimal places, with room for
4 digits left of the decimal point preceded
by a dollar sign and center justified across 10 spaces ...
" $  27.00  $   3.14 "
'''
# edit the assignment statement below
s = f'{f"$ {x:6.2f}":^10}{f"$ {y:6.2f}":^10}'
# print and echo back the formatted string which is stored in local variable
print(f"#10 ...\n{s}")
