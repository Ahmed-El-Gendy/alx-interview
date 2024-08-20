#!/usr/bin/python3
"""
Min steps to reach
"""


def minOperations(n):
    """ Minimum operations to reach n """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
