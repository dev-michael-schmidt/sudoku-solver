"""Solve a sudoku puzzle using the AnnotatedBoard() class."""

# import time
import random
from annotated_board import AnnotatedBoard


ab = AnnotatedBoard()
ab.from_file('hard1.sudoku')


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
    unknowns = deduce(board)
    while unknowns > 0:
        unknown_pass = deduce(board)
        if unknown_pass < unknowns:
            unknowns = unknown_pass

    if unknowns == 0:
        return

    if board.is_valid():
        col = random.randint(0, 8)
        row = random.randint(0, 8)

        while isinstance(board.element(row, col), int):
            col = random.randint(0, 8)
            row = random.randint(0, 8)

            s = board.get_element(row, col)

            stack = []

            for _ in range(len(s)):
                stack.append((s.pop(), board))
