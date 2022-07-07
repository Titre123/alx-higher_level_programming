#!/usr/bin/python3
'''Module 4-inherit_from.py
Check if obj is an instance of a class that inherit from a_class
'''


def inherits_from(obj, a_class):
    '''
    return True if obj is an instance of a class that inherit from a_class
    and false if it is not

    Args:
        -obj
        -a_class
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    else:
        return False
