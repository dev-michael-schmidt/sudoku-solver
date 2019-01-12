#include "globals.h"
#include "cell.h"
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

bool AnnotatedBoard::row_eliminate(int row) {
	if (row > -1) {
		set<int> s;

		for (int c = 0; c < 9; c++)
			if (board[row][c].get_value())
				s.insert(board[row][c].get_value());

		for (int c = 0; c < 9; c++) {
			if (!board[row][c].get_value()) {
				for (int v : s) {
					board[row][c].remove_possible(v);
					if (board[row][c].impossible())
						return false;
				}
			}
		}
	}
	else {
		for (int r = 0; r < 9; r++)
			this->row_eliminate(r);
	}

	return true;
}

bool AnnotatedBoard::col_eliminate(int col) {
	if (col > -1) {
		set<int> s;

		for (int r = 0; r < 9; r++)
			if (board[r][col].get_value())
				s.insert(board[r][col].get_value());

		for (int r = 0; r < 9; r++) {
			if (!board[r][col].get_value()) {
				for (int v : s) {
					board[r][col].remove_possible(v);
					if (board[r][col].impossible())
						return false;
				}
			}
		}
	}
	else {
		for (int c = 0; c < 9; c++)
			this->col_eliminate(c);
	}

	return true;
}
