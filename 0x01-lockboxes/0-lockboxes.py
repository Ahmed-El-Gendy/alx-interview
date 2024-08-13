#!/usr/bin/python3
"""
Check if I can open all boxes with DFS
"""

visit = set()
sz = 0

def dfs(node, boxes):
    visit.add(node)
    for i in boxes[node]:
        if i not in visit and i < sz:
            dfs(i, boxes)

def canUnlockAll(boxes):
    global sz
    visit.clear()
    sz = len(boxes)
    dfs(0, boxes)
    return len(visit) == len(boxes)
