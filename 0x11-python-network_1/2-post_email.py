#!/usr/bin/python3
"""
    Python script that takes in a URL and an email,
     sends a POST request to the passed URL with the
     email as a parameter, and displays the body
     of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    args = sys.argv
    value = {'email': args[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(args[1], data=data)
    with urllib.request.urlopen(req) as response:
        response = response.read()
        print(response.decode('ISO-8859-1').encode('utf-8'))
