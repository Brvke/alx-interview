#!/usr/bin/python3
""" a module for the min operations function """


def minOperations(n: int) -> int:
    """ returns the minimum number of addition and
        multiplication required to make n starting from 1
    """

    if n <= 1:
        return 0

    return factor_recursion(n)


def factor_recursion(n: int) -> int:
    """ a recursive function that finds the answer
        by the idea that the min operation is found by multiplying
        the second biggest factor with the second smallest factor
    """

    if n == 1:
        return 1

    if n <= 0:
        return 0

    flag = 0
    # a loop to find the smallest factor for n
    for i in range(2, n + 1):
        if n % i == 0:
            # if the smallest factor of n is not itself
            # i.e if n is not prime set the flag to i and break out of loop
            if n != i:
                flag = i
            break

    # if n is prime return n since it takes n amount of steps to create n
    if flag == 0:
        return n
    # this basically means the easiest step is add the second biggest factor
    else:
        return flag + factor_recursion(int(n / flag))
