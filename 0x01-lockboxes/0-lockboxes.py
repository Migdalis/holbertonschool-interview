#!/usr/bin/python3
""" Module Lockboxes """


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
    unlocked = [0]
    for i in unlocked:
        for k in boxes[i]:
            if not k in unlocked and k < len(boxes):
                    unlocked.append(k)
    if len(unlocked) == len(boxes):
        return True
    return False
