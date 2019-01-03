from itertools import chain, combinations

def one_element_subset(ss):
    return chain(*map(lambda x: combinations(ss, x), range(1, 2)))

class AnnotatedBoard:
    def __init__(self):
        self.board = [[set({i for i in range(1, 10)}) for _ in range(9)] for _ in range(9)]

    def __repr__(self):
        return "AnnotatedBoard()"

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

    def from_file(self, filename):
        with open(filename, 'r') as f:
            for r in range(9):
                row = f.readline()
                for c in range(0, 18, 2):
                    if row[c] != '.':
                        self.board[r][int(c / 2)] = int(row[c])

        self.row_elimination()
        self.col_elimination()
        self.block_elimination()

    def row_deduce(self):
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
                                self.board[r][c] = subset

    def col_deduce(self):
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
                                self.board[r][c] = subset


    def block_deduce(self):
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
                    if flag:
                        for r in range(row_start, row_start + 3):
                            for c in range(col_start, col_start + 3):
                                if isinstance(self.board[r][c], set):
                                    if subset.issubset(self.board[r][c]):
                                        self.board[r][c] = subset

    def row_elimination(self):
        for r in range(9):
            s = set({})
            for c in range(9):
                if isinstance(self.board[r][c], int):
                    s.add(self.board[r][c])

            for c in range(9):
                if isinstance(self.board[r][c], set):
                    self.board[r][c] -= s

    def col_elimination(self):
        for c in range(9):
            s = set({})
            for r in range(9):
                if isinstance(self.board[r][c], int):
                    s.add(self.board[r][c])

            for r in range(9):
                if isinstance(self.board[r][c], set):
                    self.board[r][c] -= s

    def block_elimination(self):
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

    def resolve(self):
        action = False
        for r in range(9):
            for c in range(9):
                if isinstance(self.board[r][c], set):
                    if len(self.board[r][c]) == 1:
                        self.board[r][c] = self.board[r][c].pop()
                        action = True

        return action


    def solve(self):
        count = 0
        while(self.resolve()):
            self.row_deduce()
            self.row_elimination()

            self.col_deduce()
            self.col_elimination()

            #self.block_deduce()
            self.block_elimination()
            count +=1

        print('total passes', count)
