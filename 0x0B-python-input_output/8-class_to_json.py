#!/usr/bin/python3
"""Module 8-class_to_json.
returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    '''
    returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args
        - obj: object to be coverted to dictionary
    '''
    return obj.__dict__
