#!/usr/bin/env python3

""" PMcG | 2022
    Fizzbuzz challenge """

def main():

    # create a range of numbers from 1 to 100
    numbers = range(1,101)

    # begin to loop through each number in the range and check if each number meets certain criteria
    for number in numbers:

        # check if number is multiple of 3 and 5, if so print number and "FizzBuzz"
        if number % 3 == 0 and number % 5 == 0:
            print(number, " FizzBuzz")

        # check if number is a multiple of 3, if so print number and "Fizz"   
        elif number % 3 == 0:
            print(number, " Fizz")

        # check if number is a multiple of 5, if so print number and "Buzz"
        elif number % 5 == 0:
            print(number, " Buzz")

        # if no conditions are met just print out the number
        else:
            print(number)

main()


