#!/usr/bin/python3
'''
    Python script that takes in a letter and sends a
     POST request to http://0.0.0.0:5000/search_user
     with the letter as a parameter.
'''


import requests
import sys
if __name__ == "__main__":
     q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        d = r.json()
        if d:
            print(f"[{d.get(id)}] {d.get(name)}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
