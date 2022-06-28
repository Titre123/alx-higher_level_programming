#!/usr/bin/python3
"""
Module add-integer
Adds two integer together
"""


def add_integer(a, b=98):
    '''
    This function add a and b together
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
