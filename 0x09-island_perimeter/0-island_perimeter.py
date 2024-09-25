#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the pm of the island described in the grid.

    Args:
    A 2D grid where 0 and 1 represents water and land respectively.

    Returns:
    int: The pm of the island.
    """
    pm = 0
    r = len(grid)
    c = len(grid[0]) if r else 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                pm += 4

                if i > 0 and grid[i-1][j] == 1:
                    pm -= 2  # Top neighbor
                if j > 0 and grid[i][j-1] == 1:
                    pm -= 2  # Left neighbor

    return pm
