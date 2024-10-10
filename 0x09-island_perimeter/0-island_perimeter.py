#!/usr/bin/python3
"""
Perimeter of the island
"""


def island_perimeter(grid):
    """
    Return Perimeter of the island
    """
    h = len(grid)
    w = len(grid[0])
    perimeter = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
