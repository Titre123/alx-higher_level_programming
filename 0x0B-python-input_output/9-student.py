#!/usr/bin/python3
'''
Create a class Student and instantiate it
with first_name, last_name and age
public instance method: to_json
'''


class Student:
    '''
    Instantiate with first_name, last_name and age

    Public instance Attribute
        - first_name
        - last_name
        - Age
    public instance method:
        - to_json
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Instantiate with first_name, last_name and age

        Public instance Attribute
            - first_name
            - last_name
            - Age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        return dictionary representation of instance
        of student
        '''
        return self.__dict__
