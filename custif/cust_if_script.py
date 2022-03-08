#!/usr/bin/env python3
"""PMcG | Test script
   Writing a script using if, elif, else"""

# prompt the user to enter their firstname
first_name = input("Please enter your first name...")

def main():

    # check if the firstname start with an a; convert to lower to ignore case from user input
    if first_name.lower().startswith('a') == True:
        print("Your name starts with the first letter of the alphabet")

    # check if the firstname start with an a; convert to lower to ignore case from user input
    elif first_name.lower().startswith('b') == True:
        print("Bzzzzz - your name starts with B!")

    #check if the firstname is 'Paul'; converted to lower to ignore case from user input
    elif first_name.lower() == "paul":
        print("You are in good company")

    # the catch-all statement if user input meets none of our conditions
    else:
        print("I am not interested in your name")

main()
