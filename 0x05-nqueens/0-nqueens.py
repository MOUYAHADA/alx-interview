#!/usr/bin/python3
"""N-Queens Solution Finder Module.
"""
import sys

def get_input():
    """Retrieves and validates the command-line argument for the chessboard size.

    Returns:
        int: The size of the chessboard (N).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be a number greater than or equal to 4")
        sys.exit(1)
    return n

def is_attacking(pos0, pos1):
    """Determines if two queens threaten each other.

    Args:
        pos0 (tuple): The position of the first queen.
        pos1 (tuple): The position of the second queen.

    Returns:
        bool: True if the queens can attack each other, otherwise False.
    """
    return (pos0[0] == pos1[0] or pos0[1] == pos1[1] or
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))

def build_solution(n, row=0, group=[]):
    """Recursively builds a solution for the N-Queens problem.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being processed.
        group (list): The current arrangement of valid positions.
    """
    if row == n:
        print(group)
        return
    for col in range(n):
        pos = (row, col)
        if all(not is_attacking(pos, (r, c)) for r, c in group):
            build_solution(n, row + 1, group + [pos])

n = get_input()
build_solution(n)
