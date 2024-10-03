#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    
    Args:
    x (int): The number of rounds.
    nums (list): An array of n values for each round.
    
    Returns:
    str: Name of the player that won the most rounds ("Maria" or "Ben").
         Returns None if the winner cannot be determined.
    """
    def sieve_of_eratosthenes(n):
        """Generate prime numbers up to n using Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    def count_primes(n):
        """Count the number of primes up to n."""
        primes = sieve_of_eratosthenes(n)
        return sum(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n)
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
