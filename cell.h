#ifndef CELL_H
#define CELL_H

#include "globals.h"

class Cell {
	public:
		Cell() : p(set<int>({ 1, 2, 3, 4, 5, 6, 7, 8, 9 }), v(0) {}
		~Cell() {}

		int get_value() { return v; }
		void set_value(int _v) { 
			v = _v; 
			p.clear(); 
		}
		
		set<int>& get_possible() { return p; }
		void set_possible(const set<int> & _s) { for (int i : _s) p.insert(i); }
		void remove_possible(int _v) {
			p.erase(_v);
			if (p.size() == 1) {
				v = *p.begin();
				p.clear();
			}
		}

	private:
		int v;
		set<int> p;
};
#endif // !CELL_H

