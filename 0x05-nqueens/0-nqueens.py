#!/usr/bin/python3
"""A solution to the N-Queens problem."""
import sys


def solveNqueen(n):
    """Sets up environment for backtrack."""
    col = set()  # Columns where queens are placed
    posdiag = set()  # Positive diagonals
    negdiag = set()  # Negative diagonals
    result = []

    def backtrack(r, board):
        if r == n:
            result.append(board.copy())
            return

        for c in range(n):
            if c in col or (r + c) in posdiag or (r - c) in negdiag:
                continue

            # Place the queen
            col.add(c)
            posdiag.add(r + c)
            negdiag.add(r - c)
            board[r] = c  # Store the column position of the queen

            # Recur to place the next queen
            backtrack(r + 1, board)

            # Remove the queen and backtrack
            col.remove(c)
            posdiag.remove(r + c)
            negdiag.remove(r - c)
            board[r] = None  # Reset the position

    board = [None] * n  # Initialize the board
    backtrack(0, board)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solveNqueen(N)
    
    for solution in solutions:
        # Format the output as required
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)
