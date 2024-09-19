#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): A list of coin denominations available
    total (int): The target amount

    Returns:
    int: Fewest number of coins needed to meet total, or -1 if not possible
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1

        if total == 0:
            return coin_count

    return -1
