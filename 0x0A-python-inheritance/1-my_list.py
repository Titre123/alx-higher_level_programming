#!/usr/bin/python3
'''
Module: 1-my_list.py
Create a class that inherit from list'''

class MyList(list):
    '''
    inherits from list
    
    Args:
        - list
    '''
    

    def __init__(self):
        '''
        initialize the list superclass'''
        list.__init__(self)

    def print_sorted(self):
        '''
        print the list in ascending order
        '''
        new_list = self[:]
        print('{}'.format(sorted(new_list)))
