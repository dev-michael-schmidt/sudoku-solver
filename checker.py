class SudokuChecker:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            res = self.checkRow(row)
            if not res:
                return False

        col = set({})
        for c in range(9):
            for r in range(9):
                if board[r][c] != '.':
                    if board[r][c] in col:
                        return False
                    else:
                        col.add(board[r][c])

            col = set({})

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                res = self.checkBlock(board, row, col)
                if not res:
                    return False

        return True


    def checkRow(self, row):
        s = set({})

        for num in row:
            if num != '.':
                if num in s:
                    return False
                else:
                    s.add(num)

        return True

    def checkBlock(self, board, row_start, col_start):
        s = set({})

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if board[row][col] != '.':
                    if board[row][col] in s:
                        return False
                    else:
                        s.add(board[row][col])

        return True
