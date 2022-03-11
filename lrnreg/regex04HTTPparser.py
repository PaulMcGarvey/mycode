#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
the requests library."""

# standard library imports go above 3rd party imports (best practice)
import re

# python3 -m pip install requests
import requests

def main():
    """Search a website's content"""

    while True:

            print("Where should we search?")
            url = input("> ")  # collect user input

            print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
            searchFor = input("> ")

            resp = requests.get(url)  # Send HTTP GET
            searchMe = resp.text      # strip everything off the response as a string (text)

            # use the re.search() to determine if our website has the pattern we are looking for
            # it works by taking arguments, the first is the regex search pattern, and the second
            # is the string to search within

            if re.search(searchFor, searchMe):
                print("Found a match!")
            else:
                print("No match!")

            num_of_matches = len(re.findall(searchFor, searchMe))

            print(f"There were {num_of_matches} matches on the page")

            carryOn = input("Would you like to carry out another search? Enter any key or Q to quit: ")

            if carryOn.lower() == "q":
                break


if __name__ == "__main__":
    main()
