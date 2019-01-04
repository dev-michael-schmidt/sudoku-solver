from itertools import chain, combinations

def one_element_subset(ss):
    return chain(*map(lambda x: combinations(ss, x), range(1, 2)))

class AnnotatedBoard:
    def __init__(self):
        self.board = [[set({i for i in range(1, 10)}) for _ in range(9)] for _ in range(9)]

    def __repr__(self):
        unknown = self.unknown_count()
        return "AnnotatedBoard(), known {k}".format(
            k=81-unknown,
        )

    def __str__(self):
        s = ''
        for r in range(9):
            for c in range(9):
                if c % 3 == 0 and c != 0:
                    s += '| '
                if isinstance(self.board[r][c], int):
                    s += str(self.board[r][c]) + ' '
                else:
                    s += '. '

            if r % 3 == 2 and r != 8:
                s += '\n------+-------+------\n'
            else:
                s += '\n'
        return s

    def test(self):
        for r in range(9):
            for c in range(9):
                print(self.board[r][c], end=' ')
            print()

    def elements_as_str(self):
        temp = self.board()

        for r in range(9):
            for c in range(9):
                if isinstance(temp[r][c], int):
                    temp[r][c] = str(temp[r][c])
                else:
                    temp[r][c] = '.'
        return temp

    def from_list_of_lists(self, board):
        self.board = board

        self.full_elimination()
        self.unknowns = self.unknown_count()

    def from_file(self, filename):
        with open(filename, 'r') as f:
            for r in range(9):
                row = f.readline()
                for c in range(0, 18, 2):
                    if row[c] != '.':
                        self.board[r][int(c / 2)] = int(row[c])

        if not self.full_elimination()
        self.unknowns = self.unknown_count()

    def unknown_count(self):
        '''

        :rtype: int    Number of cells which don't contain values
        '''
        count = 0
        for r in range(9):
            for c in range(9):
                if isinstance(self.board[r][c], set):
                    count += 1
        return count

    def row_deduce(self):
        '''

        :rtype: bool    True if board is valid, otherwise False
        '''
        for r in range(9):
            s = set({})
            for c in range(9):
                if isinstance(self.board[r][c], set):
                    s = s.union(self.board[r][c])

            subsets = [set({e}) for e in s]
            for subset in subsets:
                flag = False

                for c in range(9):
                    if isinstance(self.board[r][c], set):
                        if subset.issubset(self.board[r][c]):
                            if not flag:
                                flag = True
                            else:
                                flag = False
                                break
                if flag:
                    for c in range(9):
                        if isinstance(self.board[r][c], set):
                            if subset.issubset(self.board[r][c]):
                                self.board[r][c] = subset.pop()
                                self.unknowns -= 1
                                return self.full_elimination(row=r, col=c)
        return True

    def col_deduce(self):
        '''

        :rtype: bool    True if board is valid, otherwise False
        '''
        for c in range(9):
            s = set({})
            for r in range(9):
                if isinstance(self.board[r][c], set):
                    s = s.union(self.board[r][c])

            subsets = [set({e}) for e in s]
            for subset in subsets:
                flag = False

                for r in range(9):
                    if isinstance(self.board[r][c], set):
                        if subset.issubset(self.board[r][c]):
                            if not flag:
                                flag = True
                            else:
                                flag = False
                                break
                if flag:
                    for r in range(9):
                        if isinstance(self.board[r][c], set):
                            if subset.issubset(self.board[r][c]):
                                self.board[r][c] = subset.pop()
                                self.unknowns -= 1
                                return self.full_elimination(row=r, col=c)
        return True

    def block_deduce(self):
        '''

        :rtype: bool    True if board is valid, otherwise False
        '''
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                s = set({})
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        if isinstance(self.board[r][c], set):
                            s = s.union(self.board[r][c])

                subsets = [set({e}) for e in s]
                for subset in subsets:
                    flag = False

                    for r in range(row_start, row_start + 3):
                        for c in range(col_start, col_start + 3):
                            if isinstance(self.board[r][c], set):
                                if subset.issubset(self.board[r][c]):
                                    if not flag:
                                        flag = True
                                    else:
                                        flag = False
                                        break
                        else:
                            continue
                        break

                    if flag:
                        for r in range(row_start, row_start + 3):
                            for c in range(col_start, col_start + 3):
                                if isinstance(self.board[r][c], set):
                                    if subset.issubset(self.board[r][c]):
                                        self.board[r][c] = subset.pop()
                                        self.unknowns -= 1
                                        return self.full_elimination(row=r, col=c)
                            else:
                                continue
                            break
        return True

    def row_elimination(self, row=None):
        '''

        :rtype: bool    True if board is valid, otherwise False
        '''
        if row is not None:
            s = set({})
            for c in range(9):
                if isinstance(self.board[row][c], int):
                    s.add(self.board[row][c])

            for c in range(9):
                if isinstance(self.board[row][c], set):
                    self.board[row][c] -= s
                    if not len(self.board[row][c]):
                        return False
        else:
            for r in range(9):
                s = set({})
                for c in range(9):
                    if isinstance(self.board[r][c], int):
                        s.add(self.board[r][c])

                for c in range(9):
                    if isinstance(self.board[r][c], set):
                        self.board[r][c] -= s
                        if not len(self.board[r][c]):
                            return False
        return True


    def col_elimination(self, col=None):
        '''

        :rtype: bool    True if board is valid, otherwise False
        '''
        if col is not None:
            s = set({})
            for r in range(9):
                if isinstance(self.board[r][col], int):
                    s.add(self.board[r][col])

            for r in range(9):
                if isinstance(self.board[r][col], set):
                    self.board[r][col] -= s
                    if not len(self.board[r][col]):
                        return False
        else:
            for c in range(9):
                s = set({})
                for r in range(9):
                    if isinstance(self.board[r][c], int):
                        s.add(self.board[r][c])

                for r in range(9):
                    if isinstance(self.board[r][c], set):
                        self.board[r][c] -= s
                        if not len(self.board[r][c]):
                            return False
        return True

    def block_elimination(self, row=None, col=None):
        '''

        :rtype: bool    True if board is valid, otherwise False
        '''
        if row is not None and col is not None:
            row_start = row
            while row_start % 3:
                row_start -= 1

            col_start = col
            while col_start % 3:
                col_start -= 1

            s = set({})

            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    if isinstance(self.board[r][c], int):
                        s.add(self.board[r][c])

            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    if isinstance(self.board[r][c], set):
                        self.board[r][c] -= s
                        if not len(self.board[r][c]):
                            return False
        else:
            for row_start in range(0, 9, 3):
                for col_start in range(0, 9, 3):

                    s = set({})

                    for r in range(row_start, row_start + 3):
                        for c in range(col_start, col_start + 3):
                            if isinstance(self.board[r][c], int):
                                s.add(self.board[r][c])

                    for r in range(row_start, row_start + 3):
                        for c in range(col_start, col_start + 3):
                            if isinstance(self.board[r][c], set):
                                self.board[r][c] -= s
                                if not len(self.board[r][c]):
                                    return False
        return True

    def full_elimination(self, row=None, col=None):
        '''

        :rtype: bool    True if board is valid, otherwise False
        '''
        if self.row_elimination(row):
            if self.col_elimination(col):
                if self.block_elimination(row, col):
                    return True

        return False

    def solve(self):
        while self.unknowns > 0:
            self.row_deduce()

            if self.unknowns > 0:
                self.col_deduce()

            if self.unknowns > 0:
                self.block_deduce()
