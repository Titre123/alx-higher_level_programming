#!/usr/bin/python3
'''
    Python script that takes in a letter and sends a
     POST request to http://0.0.0.0:5000/search_user
     with the letter as a parameter.
'''


import requests
import sys
if __name__ == "__main__":
    args = sys.argv
    value = {}
    if args[1]:
        value = {'q': args[2]}
    else:
        value = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        r = r.json()
        if r:
            print(f"[{r.id}] {r.name}")
        else:
            print("")
    except ValueError:
        print("Not a valid JSON")
