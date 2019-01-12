sudoku_solver: globals.h main.cpp annotated_board.o
	g++ --std=c++11 main.cpp annotated_board.o -o sudoku_solver

annotated_board.o: globals.h cell.h annotated_board.cpp
	g++ --std=c++11 -c annotated_board.cpp -o annotated_board.o

clean:
	rm *.o
	rm sudoku_solver
