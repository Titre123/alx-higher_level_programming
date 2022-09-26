#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status in the specified format"""


if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen('req') as response:
        response = response.read()
        print("Body response:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode('ISO-8859-1')}")
