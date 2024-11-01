#!/usr/bin/python3
"""
validUTF8 function that determines if a given data
set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """determines if a given data set represents
    a valid UTF-8 encoding."""
    num_keys = 0
    for x in data:
        if x > 256:
            x %= 256
        if num_keys == 0:
            if (x >> 5) == 0b110:
                num_keys = 1
            elif (x >> 4) == 0b1110:
                num_keys = 2
            elif (x >> 3) == 0b11110:
                num_keys = 3
            elif (x >> 7) != 0:
                return False
        else:
            if (x >> 6) != 0b10:
                return False
            num_keys -= 1
    return num_keys == 0
