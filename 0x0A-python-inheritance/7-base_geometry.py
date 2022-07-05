#!/usr/bin/python3
'''Module 6-base_geometry.py
Add integer_validator method to the basegrometry
'''


class BaseGeometry:
    '''
    Public instance method:
        - def area(self)
        - def integer_validator(self, name, value):
    '''

    def area(self):
        '''
        Public instance method
            - raise exception
        '''
        raise Exception('Public instance method')

    def integer_validator(self, name, value):
        '''
        Public instance method
            - validates the value argument
        '''
        if type(value) == int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
