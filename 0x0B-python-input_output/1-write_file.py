#!/usr/bin/python3
"""Module 1-write_file.
Write a string to a text file and return the number of characters
"""


def write_file(filename="", text=""):
    '''
    Write a string to a text file and return the number of characters

    Args
        - filename: name of the file
        - text: string to write into file
    '''
    with open('filename', mode="w+") as new:
        return new.write(text)
