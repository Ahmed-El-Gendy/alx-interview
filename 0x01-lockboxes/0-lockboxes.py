#!/usr/bin/python3
"""
Lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened
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


'''
DFS code but have one error

#!/usr/bin/python3
"""
Check if all boxes can be opened using DFS
"""


def dfs(node, boxes, visit):
    """
    Perform DFS to visit all nodes reachable from the current node.
    """
    visit.add(node)
    for key in boxes[node]:
        if key not in visit and key < len(boxes):
            dfs(key, boxes, visit)


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    """
    visit = set()
    dfs(0, boxes, visit)
    return len(visit) == len(boxes)
'''
