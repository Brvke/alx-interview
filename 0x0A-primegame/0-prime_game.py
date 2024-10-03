#!/usr/bin/python3
"""
    An Implementation of the prime_game interview Question
"""


def sieve_of_eratosthenes(n):
    """Generate prime numbers up to n using Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]


def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for prime in primes if prime <= n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
