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
        value = {'q': args[1]}
    else:
        value = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        r = r.json()
        if r:
            print(f"[{r.get(id)}] {r.get(name)}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
