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

            searchTerms = searchFor.split()

            for term in searchTerms:
            
                if re.search(term, searchMe):
                    print(f"Found a match for {term}!")
                else:
                    print("No match!")

                num_of_matches = len(re.findall(term, searchMe))

                print(f"There were {num_of_matches} matches for {term} on the page")

            carryOn = input("Do you wish to search again? Hit any key or enter Q to quit: ")

            if carryOn.lower() == "q":
                break
    
if __name__ == "__main__":
    main()
