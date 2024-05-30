#!/usr/bin/python3
"""Module to convert CSV to json format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """converts a CSV file to a json file.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print("File not found.")
        return False
