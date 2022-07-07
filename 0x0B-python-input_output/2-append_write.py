#!/usr/bin/python3
"""Module 2-append_write.
Appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    '''
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args
        - filename: name of the file
        - text: string to append into file
    '''
    with open('filename', 'a+') as f:
        return f.write(text)
