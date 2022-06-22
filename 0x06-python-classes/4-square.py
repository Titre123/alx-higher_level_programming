#!/usr/bin/python3

class Square:
    '''Private instance attribute: size.'''

    def __int__(self, size=0):
        """Initializes the data."""
        self.__size = size

    def area(self):
        return self.__size * self.__size
    
    @property
    def size(self):
         """Sets the size to a value."""
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
