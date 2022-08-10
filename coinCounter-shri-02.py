'''
Program: Coin Counter
Author: Shrikant Sharma
Description: This program computes the number of each type of coin, the value of each type of coin and the total monetary value represented.
Filename: coinCounter-shri-02.py
Purpose: Compute the coin counter report
Revisions:
    00: announce and get the coin string from the user
    01: compute the coin counter report and print the result
'''
# there are no import statements
# there are no class definitions
# there are no function definitions
# title of the program
print("Program to count coins and calculate values")
# STEP 1: Announce, prompt, & get the coin string from the user
# announce
coin_string = input("Enter coin string: ").lower()
'''
Declare and define count_list variable of list type for storing list of coin types
and coin_value variable of list type for storing list of different types of coin values.
'''
coin_list = ['Pennies', 'Nickels', 'Dimes',
             'Quarters', 'Half-dollars']  # List of Coin type
coin_value = [0.01, 0.05, 0.10, 0.25, 0.50]  # List of coin type values
# p_count variable to store the count of penny coins
p_count = coin_string.count('p')
# n_count variable to store the count of nickel coins
n_count = coin_string.count('n')
# d_count variable to store the count of dime coins
d_count = coin_string.count('d')
# q_count variable to store the count of quarter coins
q_count = coin_string.count('q')
# h_count variable to store the count of half-dollar coins
h_count = coin_string.count('h')
total_coin_value_list = [coin_value[0]*p_count, coin_value[1]*n_count,
                         coin_value[2]*d_count, coin_value[3]*q_count, coin_value[4]*h_count]  # List of total coin values of each coin type
# STEP 2: Compute the coin counter report and echo back the result
print('='*36)
print(f"{'Coin Counter Report':^36}")
print('='*36)
print()
print(f"{'Coin':<15}{'Value':<7}{'Number':<8}{'Amount'}")
print(f"{'='*4:<15}{'='*5:<7}{'='*6:<8}{'='*6}")
print(f"{coin_list[0]:<15}{'$':1}{f'{coin_value[0]:.2f}':<8}{p_count:<6}{'$':<2}{coin_value[0]*p_count:.2f}")
print(f"{coin_list[1]:<15}{'$':1}{f'{coin_value[1]:.2f}':<8}{n_count:<6}{'$':<2}{coin_value[1]*n_count:.2f}")
print(f"{coin_list[2]:<15}{'$':1}{f'{coin_value[2]:.2f}':<8}{d_count:<6}{'$':<2}{coin_value[2]*d_count:.2f}")
print(f"{coin_list[3]:<15}{'$':1}{f'{coin_value[3]:.2f}':<8}{q_count:<6}{'$':<2}{coin_value[3]*q_count:.2f}")
print(f"{coin_list[4]:<15}{'$':1}{f'{coin_value[4]:.2f}':<8}{h_count:<6}{'$':<2}{coin_value[4]*h_count:.2f}")
print(f"{'Total amount: ':>30}{'$':<2}{sum(total_coin_value_list):.2f}")
