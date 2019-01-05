"""Solve a sudoku puzzle using the AnnotatedBoard() class."""

import time
import random
from annotated_board import AnnotatedBoard


def deduce(board):
    """
    Deduce values from the board and return number of unknowns.

    """
    board.full_deduce()
    return board.unknown_count()


def depth_first_search(board):
    """
    Search using DFS when deductions can't be made, otherwise deduce values.

    :board:     AnnotatedBoard() object
    :rtype:     None
    """

    # Base case
    count = deduce(board)
    while count:
        next = deduce(board)
        if next < count:
            count = next
        else:
            break

    if not count:
        return True

    # Search case
    if board.is_valid():
        col = random.randint(0, 8)
        row = random.randint(0, 8)

        while isinstance(board.element(row, col), int):
            col = random.randint(0, 8)
            row = random.randint(0, 8)

        s = board.element(row, col)

        for _ in range(len(s)):
            board.guess(row, col, s.pop())
            if depth_first_search(board):
                return True

    return False



ab = AnnotatedBoard()
ab.from_file('medium33.sudoku')
print(ab)
start = time.time()
if depth_first_search(ab):
    stop = time.time()
    print('SUCCESS', stop-start)
    print()
print(ab)
