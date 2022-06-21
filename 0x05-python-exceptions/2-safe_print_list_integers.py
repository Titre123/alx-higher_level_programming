#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
   for i in range(0,x):
       string = ""
       try:
           if my_list[i].isdigit() == true:
               string += my_list[i]
            else:
                pass
            print(f'{string}\n')
            last_char = string[-1]
            length = string.index(last_char) + 1
            return length
        except:
