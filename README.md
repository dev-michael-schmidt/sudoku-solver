# sudoku-solver
A python program to solve sudoku puzzles.

### Files
- `*.sudoku`: a game file.  
- `annotated_board.py`: contains an `AnnotatedBoard` class which holds and operates on the sudoku puzzle.
- `checker.py`: a simple script to check if a puzzle contains a valid solution.  No longer maintained (use `AnnotatedBoard.is_valid()`).
- `sudoku.ipynb`: Jupyter Notebook with DFS search algorithm for puzzles where a solution can't be solved solely via deduction.

### Functions
`AnnotatedBoard`
- `self.__init__(self, board=None)`:  Initialize a blank puzzle or use an `AnnotatedBoard` to make a copy.
- `self.__repr__(self)`: for interactive interpreters. displays in Type(known, completed, validity) format.
- `self.__str__(self)`: convert the board to a print pretty format for use with `print()` function. i.e:
```
game = AnnotatedBoard()
game.from_file('hard1.sudoku')
game = DFS(game)
print(game)
5 1 9 | 7 4 8 | 6 3 2
7 8 3 | 6 5 2 | 4 1 9
4 2 6 | 1 3 9 | 8 7 5
------+-------+------
3 5 7 | 9 8 6 | 2 4 1
2 6 4 | 3 1 7 | 5 9 8
1 9 8 | 5 2 4 | 3 6 7
------+-------+------
9 7 5 | 8 6 3 | 1 2 4
8 3 2 | 4 9 1 | 7 5 6
6 4 1 | 2 7 5 | 9 8 3
```
- `self.__deepcopy__(self, memo)`:  This function may need some work, but provides a mechanism for `copy.deepcopy()` method from the standard library.
- `self.from_file()`: load a puzzle from a file using the specified format.
- `self.from_list_of_lists()`: load a puzzle from a list of lists where elements are string types (WIP).
- `self.element(row, col)`: Return the value, or set({}) of possible values at the specified row and column.
- `self.guess(row, col, value)`: Set a cell value without deduction.  Value must be a possible value for that cell. (Use `element()` for a set of values)
    - `value == -1`: reset the cell to a set of possibilities.  If cell was a value, updates internal unknown count otherwise recalculates possibilities for cell.
    - `value == {1 - 9}`: fill the cell with a value.
        - if value is accepted, returns `True` and updates internal unknown count.
- `self.unknown_count(self)`: return a count of cells without values.  Updates internal counter.
- `self.full_deduce()`: performs one iteration and deduces values (not sets of values (yet)) on a cell.  One iteration deducts value by scanning possible values in unknown cells, then if a cell contains a unique possibility, that value is placed.  This function works on the ROW, COLUMN, and BLOCK level by calling `self.row_deduce(self)`, `self.col_deduce(self)`, and `self.block_deduce(self)`.  Future work may try to deduce a set of possibilities.  For example a row/column/block containing:
    - `{1, 2, 7, 8}`, `{1, 2, 7, 8}`, `{1, 2}`, and `{1, 2}` should deduce down into `{7 ,8}`, `{7, 8}`, `{1, 2}`, and `{1, 2}`.
returns `True` if the puzzle is valid, otherwise `False`.
- `self.row_duplicate(self, row=None)`: Scans the puzzle for duplicate values occurring in a row.  If `row` is supplied, only the row is checked.  Returns `True` if a duplicate is found, otherwise `False`.
- `self.col_duplicate(self, col=None)`: Scans the puzzle for duplicate values occurring in a column.  If `col` is supplied, only the columnis checked.  Returns `True` if a duplicate is found, otherwise `False`.
- `self.col_duplicate(self, row=None, col=None)`: Scans the puzzle for duplicate values occurring in a block.  If `row` and `col` arue supplied, only the corresponding block is checked.  Returns `True` if a duplicate is found, otherwise `False`.
- `self.row_deduce(self)`: to be documented
- `self.col_deduce(self)`: to be documented
- `self.block_deduce(self)`: : to be documented
- `self.is_valid(self, row=None, col=None)`: to be documented
- `self.row_elimination(self, row=None)`: to be documented
- `self.col_elimination(self, col=None)`: to be documented
- - `self.block_elimination(self, row=None, col=None)`: to be documented





#### Format
Use dots to specify unknown cells in a plain text format.
```
2 . . . . . . 6 3
. . 6 5 8 3 . . 9
. . 4 1 . . . . 7
. 6 . . . 1 . 9 8
. 9 3 . 5 . 6 2 .
8 2 . 3 . . . 7 .
6 . . . . 9 7 . .
5 . . 6 7 8 4 . .
3 4 . . . . . . 6
```
