#ifndef ANNOTATED_BOARD_H
#define ANNOTATED_BOARD_H

#include "globals.h"
#include "cell.h"

class AnnotatedBoard {
	public:
		AnnotatedBoard();

		bool from_file(string filename);

		bool row_eliminate(int row = -1);
		bool col_eliminate(int col = -1);
		bool blk_eliminate(int row = -1, int col = -1);

	private:
		Cell** board;

};
#endif
