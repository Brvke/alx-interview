#!/usr/bin/python3
"""A solution to the N-Queens problem."""
import sys

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row, board, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)

def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve_n_queens(n, 0, [-1]*n, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
