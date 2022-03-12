#!/usr/bin/env python3
"""Returning the astronauts and which craft they are currently on"""

# import requests
import requests

# store our api url in a variable
URL= "http://api.open-notify.org/astros.json"

# define the main() function
def main():

    # make the api call and get back .json
    resp= requests.get(URL).json()

    # get the total number of astronauts and store in variable

    total_astro = len(resp['people'])

    # prints the total number of astronauts
    print(f"People in space: {total_astro}")

    # loop through each person - store their name and craft then print out in f-string

    for person in resp.get('people'):

        name = person.get('name')

        craft = person.get('craft')

        print(f"{name} is on the {craft}")


main()
