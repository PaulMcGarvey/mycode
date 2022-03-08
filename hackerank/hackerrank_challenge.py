#!/usr/bin/env python3
""" """
# Prompt the user for input - cast as an integer
n = int(input("Enter any integer..."))

# if n is odd print 'Weird'
if n % 2 != 0:
    print("Weird")

# if n is even and inbetween 2 and 5 inclusively print 'Not weird' 
elif n % 2 == 0 and (2<=n<=5):
    print("Not weird")

# if n is even and inbetween 6 and 20 inclusively print 'Weird'
elif n % 2 == 0 and (6<=n<=20):
    print("Weird")

# if n is even and greater than 20 print 'Not weird'   
elif n % 2 == 0 and n > 20:
    print("Not weird")
