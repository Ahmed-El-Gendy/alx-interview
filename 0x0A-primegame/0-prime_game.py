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

    Maria = Ben = 0

    for num in nums:
        if num < 2:
            Ben += 1
            continue

        sieve = [True] * (num + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(num ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, num + 1, i):
                    sieve[j] = False

        primes = [i for i in range(2, num + 1) if sieve[i]]
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
