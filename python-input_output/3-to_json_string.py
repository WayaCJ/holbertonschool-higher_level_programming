#!/usr/bin/python3
"""module for the function that returns
the JSON representation of an object"""


import json

def to_json_string(my_obj):
    """defines the json representation of an object"""
    return json.dumps(my_obj)
