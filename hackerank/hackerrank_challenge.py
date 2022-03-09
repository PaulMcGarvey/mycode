#!/usr/bin/env python3

""" PMcG | 2022
    Trying to complete the hackerank challenge"""

def main():

    # Prompt the user for input - cast as an integer
    n = int(input("Enter any integer..."))

    # check if user loves the hoops
    if n == 67 or n == 1888:
        print("In the heat of Lisbon, fans came in their thousands, to see the bhoys become, champions, sixty seven...")
        return

    # if n is odd print 'Weird'
    if n % 2 != 0:
        print("Weird - this number is odd")

    # if n is even and inbetween 2 and 5 inclusively print 'Not weird' 
    elif n % 2 == 0 and (2<=n<=5):
        print("Not weird - this number is even and between 2 and 5 (inclusive)")

    # if n is even and inbetween 6 and 20 inclusively print 'Weird'
    elif n % 2 == 0 and (6<=n<=20):
        print("Weird - this number is even and between 6 and 20 (inclusive)")

    # if n is even and greater than 20 print 'Not weird'   
    elif n % 2 == 0 and n > 20:
        print("Not weird - this number is even and greater than 20")

main()
