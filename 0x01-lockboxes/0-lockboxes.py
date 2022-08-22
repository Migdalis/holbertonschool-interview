#!/usr/bin/python3
""" Module Lockboxes """


from operator import truediv


def search(boxes, key):
    """ Search a key in all boxes"""
    for k in boxes[key]:
        if k < len(boxes):
            return True
    return False


def canUnlockAll(boxes):
    """
        Method that determines if all
        the boxes can be opened
        Args:
            boxes: list of lists
        Return:
            True if all boxes can be opened,
            else return False
    """
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    unloked = ['U']
    print(len(boxes))
    for box in range(1, len(boxes)):
        if search(boxes, box) or box == 0:
            unloked.append('U')
    print(len(unloked))
    if len(unloked) == len(boxes):
        return True
    return False
