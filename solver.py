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
    count = board.unknown_count()
    print('new function call,', count, 'unknowns')
    print(board)
    count = deduce(board)
    print('deduced. Now', count)

    while count:
        next = deduce(board)
        print('deduced. Now', count)
        if next < count:
            count = next
        else:
            break

    print('could not deduce anymore.')
    if not count:
        return True

    # Search case
    if board.is_valid():
        print('board is valid')
        col = random.randint(0, 8)
        row = random.randint(0, 8)

        while isinstance(board.element(row, col), int):
            col = random.randint(0, 8)
            row = random.randint(0, 8)

        stack = board.element(row, col)
        reset = stack
        guess_board = board

        # need to preserve board!

        print('going to try to backtrack', stack, 'values')
        for _ in range(len(stack)):
            v = stack.pop()
            print('trying', v, 'at', row, col)
            guess_board.guess(row, col, v)
            if depth_first_search(guess_board):
                board = guess_board
                return True

        board.guess(row, col, reset)
        print('no longer back tracking')
    else:
        print('board is invalid')

    return False




ab = AnnotatedBoard()
ab.from_file('hard1.sudoku')
print(ab)
start = time.time()
if depth_first_search(ab):
    stop = time.time()
    print('SUCCESS', stop-start)
    print()
print(ab)
