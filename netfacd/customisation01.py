#!/usr/bin/env python3

""" """

# import the netifaces module
import netifaces


print(f"Valid adapters are: {netifaces.interfaces()}\n")
adapter = input("enter the name of your adapter: ")

while True:
    if adapter in netifaces.interfaces():
        print(f"The IP address of {adapter} is {netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]['addr']} ")
        break
    else:
        print(f"{adapter} is not a valid adapter name")
        break
