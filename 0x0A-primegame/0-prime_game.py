#!/usr/bin/python3
"""
    An Implementation of the prime_game interview Question
    with details explained in README.md
"""


def check_prime(num):
    """
        Args:
            num: int value to check if prime or not
        Returns:
            Boolean
    """

    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primelist(num):
    """
        Args:
            num: an int value of the number to play for
        Returns:
            a list of prime numbers from 1 upto num
    """

    # list of prime numbers from 1 until num
    prime_list = []
    for i in range(2, num + 1):
        if check_prime(i):
            prime_list.append(i)
    return prime_list


def isWinner(x, nums):
    """
        Args:
            x: an int value for the number of turns to play the game
            nums: a list of number to play for
        Returns:
            prints the winner of the game after x rounds of playing
    """

    maria = 0
    ben = 0

    if x > len(nums):
        return None

    for i in range(x):
        prime = primelist(nums[i])
        if len(prime) == 0 or len(prime) % 2 == 0:
            ben += 1
        elif len(prime) % 2 != 0:
            maria += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    elif ben == maria:
        return None
