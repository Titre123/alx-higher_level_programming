#!/usr/bin/python3
'''
Module : rectangle
rectangle script inheriting from base'''


from models.base import Base


class Rectangle(Base):
    '''
    class Rectangle inherit from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        constructor
        Private instance attribute
            - width
            - height
            - x
            - y

        public instance
            - area
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter'''
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' y setter'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        method to get the area of rectangle
        '''
        return self.__height * self.__width

    def display(self):
        '''display the area with #'''
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''
        display instance of Rectangle to user'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''Update the value of instance attributes'''
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
    def to_dictionary(self):
        '''
        return a dictionary of Rectangle instance
        '''
        my_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                   'height': self.__height, 'width': self.__width}
        return my_dict
