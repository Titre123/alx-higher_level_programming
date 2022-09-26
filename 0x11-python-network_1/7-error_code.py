#!/usr/bin/python3
"""
    Python script that takes in a URL,
     sends a request to the URL and displays
      the body of the response (decoded in utf-8)
"""


import requests
import sys
if __name__ == "__main__":
    status_code = None
    args = sys.argv
    try:
        r = requests.get(args[1])
        print(r.text)
        r.raise_for_status()
        status_code = r.status_code
    except requests.exceptions.RequestException as err:
        print(f'Error code: {status_code}')
