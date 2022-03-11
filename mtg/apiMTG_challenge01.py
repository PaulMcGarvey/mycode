#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():

    """Run time code"""

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()            # collect user input for MTG card set to lookup

    # create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")   # this "f" string reads: API + "cards/" + setcode

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    things = resp.json()
    
    no_of_cards = range(0,len(things.get('cards')))

    with open(f"{setcode}_mtg_data.index", "w") as out_file:

        for c in no_of_cards:

            print(f"{c} {things.get('cards')[c].get('name')} -- {things.get('cards')[c].get('set')} -- {things.get('cards')[c].get('imageUrl')}")
    
        #print(things.keys())

        #print(len(things.get('cards')))

        #print(f"{c}")

        #print(type(c))

        #print(f"{things.get('cards')[0]}")

if __name__ == "__main__":
    main()

