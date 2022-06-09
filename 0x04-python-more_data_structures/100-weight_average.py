#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    div = 0
    if my_list == []:
        return 0
    else:
        for a, b in my_list:
            total = total + (a * b)
            div += b
    return float(total / div)
