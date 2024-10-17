#!/usr/bin/python3
"""
Prime Game problem
"""


def isWinner(x, nums):
    """
    Determine who wins the game
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    sieve = [i for i in range(n + 1) if sieve[i]]
    wins = 0
    for i in range(x):
        wins += sieve[i] in nums

    return "Maria" if wins % 2 == 0 or wins == 0 else "Ben"
