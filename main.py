from solver import AnnotatedBoard

ab = AnnotatedBoard()
ab.from_file('puzzle.txt')

print(ab)
ab.solve()
print(ab)
