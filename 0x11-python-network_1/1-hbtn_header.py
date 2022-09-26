#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request
     to the URL and displays the value of the X-Request-Id
     variable found in the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    args = sys.argv
    req = urllib.request.Request(args[1])
    with urllib.request.urlopen(req) as response:
        response = response.info()["X-Request-Id"]
        print(response)
