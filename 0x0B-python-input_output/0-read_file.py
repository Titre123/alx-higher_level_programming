#!/usr/bin/python3
"""Module 0-read_file.
Reads from filename and prints its contents to stdout.
"""


def read_file(filename=""):
    '''
    Reads from filename and prints
    its contents to stdout.

    Args
        - filename: name of the file
    '''
    with open(file='filename') as file:
        print(file.read(), end="")
