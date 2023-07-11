#!/usr/bin/python3
"""Defines reading func"""


def read_file(filename=""):
    """Display the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
