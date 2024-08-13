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
