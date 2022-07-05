#!/usr/bin/python3
'''Module 2-is_same_class.py
lookup the attributes and methods in a class
'''


def is_same_class(obj, a_class):
    '''
    return True if obj is an instance of a_class
    and false if it is not

    Args:
        -obj
        -a_class
    '''
    if type(obj, a_class):
        return True

    else:
        return False
