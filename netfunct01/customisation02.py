#!/usr/bin/env python3

""" PMcG | 2022
    Creating a function and then calling it in main()"""

# define a function which accepts a list of ip addresses
def devicereboot(iplist):
    for ip in iplist:
        print(f"Connecting to {ip} ... REBOOTING NOW")

def main():

    ip_addresses  = ['8.8.8.8' , '192.168.0.32', '10.180.0.1', '1.2.3.4', '192.168.1.11']

    devicereboot(ip_addresses)

main()
