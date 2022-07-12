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

    def to_json(self, attrs=None):
        '''
        return dictionary representation of instance
        of student
        '''
        new_dict = dict()
        if type(attrs) is list and all([type(x) is str for x in attrs]):
            for x in attrs:
                if x in self.__dict__:
                    new_dict.update({x: self.__dict__[x]})
            return new_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            - json: dictionnary of attributes
        """
        for x in json:
            self.__dict__.update({x: json[x]})
