#!/usr/bin/python3
"""Module 7-add_item.
Adds all arguments to a Python list, and then save them to a file
"""

import sys
import os
import json

save_to_json_file = __import__('5-save_to_\
    json_file.py').save_to_json_file

load_from_json_file = __import__('6-load_from_\
    json_file.py').load_from_json_file

file = 'add_item.json'
my_list = []

if os.path.exists(file) and os.path.getsize > 0:
    load_from_json_file(file)

if len(sys.argv) > 1:
    for args in sys.argv[1:]:
        my_list.append(args)

save_to_json_file(my_list, file)
