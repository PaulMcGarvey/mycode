#! /usr/bin/env python3

""" PMcG | 2022 
    Mucking about"""

## Expirimenting with stuff

def main():
    
    # while a number has not been supplied - letters, etc
    while True:

        # ask the user to input a number
        userNumber = input("Enter an integer into the terminal: ")

        # check that the supplied input does not have letters or special characters - if so, the loop continues
        if userNumber.isnumeric() == True:
            break

        else:
            print("You did not enter a integer...")

    print(int(userNumber) * 2)



main()
