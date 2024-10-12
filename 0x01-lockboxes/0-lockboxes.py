#!/usr/bin/python3
"""
module to house the lockbox function
"""


def canUnlockAll(boxes):
    """
    function that determines if a lockbox
    can be open
    """
    # Number of boxes
    n = len(boxes)

    # Set of opened boxes, starting with the first one (box 0)
    opened_boxes = {0}

    # Set of keys we have, starting with the keys in the first box (box 0)
    keys = set(boxes[0])

    # Continue while there are unopened boxes that we have keys for
    while keys:
        new_key = keys.pop()  # Take one key from the set of available keys
        if new_key < n and new_key not in opened_boxes:
            # Open the box if it's within the range and hasn't been opened yet
            opened_boxes.add(new_key)
            # Add the keys from the newly opened box
            keys.update(boxes[new_key])

    # Return True if all boxes are opened
    return len(opened_boxes) == n
