from solver import AnnotatedBoard

ab = AnnotatedBoard()
ab.from_file('puzzle.txt')
print(ab)
print()

ab.solve()
print(ab)
