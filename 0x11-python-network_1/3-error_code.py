#!/usr/bin/python3
"""
    Python script that takes in a URL,
     sends a request to the URL and displays
      the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    args = sys.argv
    req = urllib.request.Request(args[1])
    try:
        with urllib.request.urlopen(req) as response:
            response = response.read()
            print(response)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
