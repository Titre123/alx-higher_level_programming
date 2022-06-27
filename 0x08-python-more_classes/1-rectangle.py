#!/usr/bin/python3
''' Module Documentation'''


class Rectangle:
    '''Represents a square.
    Private instance attribute: width:
        - property def width(self)
        - property setter def width(self, value)
    Private instance attribute: height:
        - Property def height(self)
        - Property def height(self, value)
    Instantiation with optional size.
    '''
    def __init__(self, width=0, height=0):
        '''Initializes the data'''

        self.width = width
        self.height = height

        @property
        def width(self):
            """Retrieves the width."""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width to a value."""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            '''Retrieves the height'''
            return self.__height

        @height.setter
        def height(self, value):
            '''Sets the height to a value'''
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
