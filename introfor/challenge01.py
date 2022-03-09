#!/usr/bin/python3
"""PMcG | 2022
   Printing dictionary data stored as lists to the screen"""


def main():
    
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"agriculture":["haggis","neeps","tatties"]}
         ]
    
    # Looping through each of the three farms in our farms list
    for farm in farms:
        print(farm.get("name", "Unknown farm"), end= ":\n")
        
        for agriculture in farm.get("agriculture"):
            print(" -", agriculture)

main()
