#!/usr/bin/python3
"""
Module print_square
prints a square with the character #
"""


def print_square(size):
    '''
    This function print a sqaure of character #
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#"*size, end="\n")
