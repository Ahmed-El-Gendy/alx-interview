#!/usr/bin/python3
"""
Check if all boxes can be opened using DFS
"""


def dfs(node, boxes):
    """
    Perform DFS to visit all nodes reachable from the current node.
    """
    visit.add(node)
    for key in boxes[node]:
        if key not in visit and key < sz:
            dfs(key, boxes)


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    """
    global sz
    visit.clear()
    sz = len(boxes)
    dfs(0, boxes)
    return len(visit) == sz
