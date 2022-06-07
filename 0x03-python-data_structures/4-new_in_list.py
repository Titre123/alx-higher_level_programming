#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a_copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return a_copy
    else:
        a_copy[idx] = element
        return a_copy
