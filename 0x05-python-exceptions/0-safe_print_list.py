#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_str = "".join(my_list)
    print(list_str)
    try:
        char = list_str[x]
        return x
    except:
        last_char = list_str[-1]
        length = list_str.index(last_char) + 1
        return length
