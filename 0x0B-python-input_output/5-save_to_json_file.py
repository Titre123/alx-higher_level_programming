#!/usr/bin/python3
"""Module 5-save_to_json_file.
Writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an Object to a text file, using a JSON representation

    Args
        - my_obj: object (string) represented in JSON
        - filename: file to write JSON representation into
    '''
    with open(file='filename', mode='w') as file:
        new_obj = json.dumps(my_obj)
        file.write(new_obj)
