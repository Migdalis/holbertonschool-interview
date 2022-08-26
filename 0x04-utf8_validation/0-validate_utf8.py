#!/usr/bin/python3
""" Module to determine if a data is a valid UTF-8 """


def validUTF8(data):
    """
        Method that determines if a given data
        set represents a valid UTF-8 encoding
    """
    try:
        bytes(data).decode("UTF-8")
    except Exception:
        return False
    return True
