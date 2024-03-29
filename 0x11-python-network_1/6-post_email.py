#!/usr/bin/python3
"""
    Python script that takes in a URL and an email,
     sends a POST request to the passed URL with the
     email as a parameter, and displays the body
     of the response (decoded in utf-8)
"""


import requests
import sys
if __name__ == "__main__":
    args = sys.argv
    data = {'email': args[2]}
    r = requests.post(args[1], data = data)
    print(r.text)
