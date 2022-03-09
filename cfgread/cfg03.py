#!/usr/bin/env python3
## create file object in "r"ead mode

#create a counter to count how many lines we have
counter = 0

with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    for line in configlist:
        counter += 1

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(f"There are {counter} lines in the file")
