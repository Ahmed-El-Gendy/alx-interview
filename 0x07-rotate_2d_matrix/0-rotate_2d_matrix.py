#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D Matrix
    """
    for a, b in enumerate(zip(*reversed(matrix))):
        matrix[a] = list(b)
