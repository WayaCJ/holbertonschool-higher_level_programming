#!/usr/bin/python3
"""Module for the function that returns an object
represented by a json string"""

import json

def from_json_string(my_str):
    """return of an object"""
    return json.loads(my_str)
