#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests

URL= "http://api.open-notify.org/iss-now.json"

import datetime

def main():
    resp= requests.get(URL).json()

    epoch_time = resp.get('timestamp')
    date_time = datetime.datetime.fromtimestamp(epoch_time)

    print("CURRENT LOCATION OF THE ISS")
    print(f"Timestamp: {date_time} " )
    print(f"Lon: {resp.get('iss_position').get('longitude')}")
    print(f"Lat: {resp.get('iss_position').get('latitude')}") 

if __name__ == "__main__":
    main()
