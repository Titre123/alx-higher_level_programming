#!/usr/bin/python3
'''Module 3-is_kind_of_class.
Finds if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class.
'''


def is_kind_of_class(obj, a_class):
    '''
    return True if obj is an instance of a_class or a superclass
    and false if it is not

    Args:
        -obj
        -a_class
    '''
    if isinstance(obj, a_class):
        return True

    else:
        return False
