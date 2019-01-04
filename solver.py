import time
import random
from board import AnnotatedBoard


ab = AnnotatedBoard()
ab.from_file('hard1.sudoku')

print()

def depth_first_search(board):
    col = random.randint(0, 8)
    row = random.randint(0, 8)

    while isinstance(board.element(row, col), int):
        col = random.randint(0, 8)
        row = random.randint(0, 8)

    s = board.get_element(row, col)

    stack = []

    for _ in range(len(s)):
        stack.append((s.pop(), board))
