#!/usr/bin/python3

class Square:
    '''Private instance attribute: size.'''

    def __init__(self, size):
        '''instantiate size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raize ValueError("size must be >= 0")
        self.__size = size
