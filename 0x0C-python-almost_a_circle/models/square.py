#!/usr/bin/python3
'''
Module : square
square script inheriting from base and rectangle'''


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Square inherit from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Returns a string representation of a Square instance."""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id,
            self.__x, self.__y, self.__width
            )

    @property
    def size(self):
        """Retrieves the size attribute."""

        return self.__width

    @size.setter
    def size(self, value):
        '''Set size attribute'''
        if type(value) == int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__size = args[1]
            if len(args) > 2:
                self.__x = args[2]
            if len(args) > 3:
                self.__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.__width = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        my_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                   'size': self.__size}
        return my_dict
