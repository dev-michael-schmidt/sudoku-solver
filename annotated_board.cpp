#include "globals.h"
#include "annotated_board.h"

AnnotatedBoard::AnnotatedBoard() {
	try {
		board = new Cell*[9];
		for (int r = 0; r < 9; r++)
			board[r] = new Cell[9];
	}
	catch (const bad_alloc & ba) {
		cerr << "bad allocation: " << ba.what() << endl;
	}
}
