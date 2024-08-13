#!/usr/bin/python3
"""
lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    """
    unlocked_boxes = set()
    keys = set(boxes[0])
    unlocked_boxes.add(0)

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.update(boxes[key])

    return len(unlocked_boxes) == len(boxes)
