#!/usr/bin/python3
"""Module 6-load_from_json_file.
Creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    '''
    Creates an Object from a “JSON file”

    Args
        - filename: file with a JSON string representation
    '''
    with open(file=filename, mode='r') as file:
        return json.load(file)
