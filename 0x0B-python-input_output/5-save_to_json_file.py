#!/usr/bin/python3
"""Writes function to Text File"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, 'w', encoding='utf-8') as fn:
        json.dump(my_obj, fn)
