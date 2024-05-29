#!/usr/bin/python3
"""Module for the function that writes an object to a
text file, using a json representation"""
import json

def save_to_json_file(my_obj, filename):
    """writing an object to a text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
