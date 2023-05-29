#pragma once
#include <iostream>
using namespace std;


class Sudoku
{
	struct Cell
	{
		int value;
		bool potentials[9]{ 1,1,1,1,1,1,1,1,1 };
		int n = 9;
		Cell() : value(0) {};
		Cell(const int value) : value(value) {};
		bool set(int value)
		{
			cout << "value: " << value << '\n';
			if (potentials[value - 1] && this->value == 0)
			{
				this->value = value;
				n = 0;
				return true;
			}
			return false;
		}
		int pop(int value)
		{
			if (this->value == 0)
			{
				if (potentials[value - 1])
				{
					potentials[value - 1] = false;
					--n;
					if (n == 1)
					{
						return update();
					}
				}
			}
			return 0;
		}
		int update()
		{
			for (int i = 0; i < 9; ++i)
			{
				if (potentials[i])
				{
					return i + 1;
				}
			}
			return 0;
		}
	};
	struct Box_number
	{
		bool potentials[3][3];
		int nx = 3;
		int ny = 3;
		int n = 9;
		int x, y;
		Box_number()
		{
			x = -1;
			y = -1;
			for (int i = 0; i < 3; ++i)
			{
				for (int j = 0; j < 3; ++j)
				{
					potentials[i][j] = 1;
				}
			}
		}
		void set(int y, int x)
		{
			this->y = y;
			this->x = x;
			for (int i = 0; i < 3; ++i)
			{
				for (int j = 0; j < 3; ++j)
				{
					potentials[i][j] = false;
					//cout << i << ' ' << j << " = false\n";
				}
			}
			ny = 0;
			nx = 0;
			n = 0;
		}
		void pop_column(int x)
		{
			if (this->x == -1)
			{
				for (int i = 0; i < 3; ++i)
				{
					if (potentials[i][x])
					{
						potentials[i][x] = false;
						--n;
					}
				}
				--nx;
			}
		}
		void pop_row(int y)
		{
			if (this->y == -1)
			{
				for (int i = 0; i < 3; ++i)
				{
					if (potentials[y][i])
					{
						potentials[y][i] = false;
						--n;
					}
				}
				--ny;
			}
		}
		bool update()
		{
			if (n == 1)
			{
				for (int i = 0; i < 3; ++i)
				{
					for (int j = 0; j < 3; ++j)
					{
						if (potentials[i][j])
						{
							set(i, j);
							cout << "y x " << i << ' ' << j << '\n';
							return true;
						}
					}
				}
			}
			return false;
		}
	};
	
	Cell arr[9][9];
	Box_number boxes[3][3][9];
public:
	Sudoku(){}
	bool set(int x, int y, int value)
	{
		bool res = false;
		if (1 <= value && value <= 9)
		{
			res = arr[y][x].set(value);
			if (res)
			{
				boxes[x / 3][y / 3][value - 1].set(y - (y / 3) * 3, x - (x / 3) * 3);
				//cout << "set box " << x / 3 << ' ' << y / 3 << ' ' << y - (y / 3) * 3 << ' ' << x - (x / 3) * 3 << '\n';
				pop_potentials_in_lines(y, x);
				pop_potentials_in_box(y, x);
				pop_potentials_in_neighbor_boxes(y, x);
			}
		}
		return res;
	}
	void pop_potentials_in_lines(int y, int x)
	{
		int temp;
		int value = arr[y][x].value;
		// update x row
		for (int i = 0; i < 9; ++i)
		{
			temp = arr[i][x].pop(value);
			if (temp)
				set(x, i, temp);
		}
		// update y column
		for (int i = 0; i < 9; ++i)
		{
			temp = arr[y][i].pop(value);
			if (temp)
				set(i, y, temp);
		}
	}
	void pop_potentials_in_box(int y, int x)
	{
		int temp;
		int value = arr[y][x].value;
		int box_x = x / 3;
		int box_y = y / 3;

		// pop cells
		for (int i = box_y * 3; i < box_y * 3 + 3; ++i)
		{
			for (int j = box_x * 3; j < box_x * 3 + 3; ++j)
			{
				temp = arr[i][j].pop(value);
				if (temp)
					set(j, i, temp);
			}
		}
		// pop numbers
		int tx = x - box_x * 3;
		int ty = y - box_y * 3;
		for (int number = 0; number < 9; ++number)
		{
			boxes[box_y][box_x][number].potentials[ty][tx] = false; // работает
		}
	}
	void pop_potentials_in_neighbor_boxes(int y, int x)
	{
		int number = arr[y][x].value - 1;
		int box_x = x / 3;
		int box_y = y / 3;
		// работает
		boxes[(box_y + 1) % 3][box_x][number].pop_column(x%3);
		boxes[(box_y + 2) % 3][box_x][number].pop_column(x - box_x * 3);
		boxes[box_y][(box_x + 1) % 3][number].pop_row(y%3);
		boxes[box_y][(box_x + 2) % 3][number].pop_row(y - box_y * 3);

		int tx, ty;
		
		for (int i = 0; i < 3; ++i)
		{
			for (int j = 0; j < 3; ++j)
			{
				for (int n = 0; n < 9; ++n)
				{
					if (boxes[i][j][n].update())
					{
						ty = boxes[i][j][n].y + i * 3;
						tx = boxes[i][j][n].x + j * 3;
						set(tx, ty, n + 1);
						cout << "p tx ty n " << tx << ' ' << ty << ' ' << n << ' ';
					}
				}
			}
		}
	}

	void print_potentials(int x, int y)
	{
		int bx = x / 3, by = y / 3;
		cout << x << ' ' << y << " potentials: ";
		for (int n = 0; n < 9; ++n)
		{
			cout << boxes[by][bx][n].potentials[y % 3][x % 3] << ' ';
		}
		cout << endl;
	}
	void print()
	{
		for (int y1 = 0; y1 < 3; ++y1)
		{
			for (int y2 = 0; y2 < 3; ++y2)
			{
				for (int x1 = 0; x1 < 3; ++x1)
				{
					for (int x2 = 0; x2 < 3; ++x2)
					{
						cout << arr[3 * y1 + y2][3 * x1 + x2].value << ' ';
					}
					cout << ' ';
				}
				cout << '\n';
			}
			cout << '\n';
		}
	}
	void print_potentials(int value)
	{
		for (int y1 = 0; y1 < 3; ++y1)
		{
			for (int y2 = 0; y2 < 3; ++y2)
			{
				for (int x1 = 0; x1 < 3; ++x1)
				{
					for (int x2 = 0; x2 < 3; ++x2)
					{
						cout << boxes[y1][x1][value - 1].potentials[y2][x2] << ' ';
					}
					cout << ' ';
				}
				cout << '\n';
			}
			cout << '\n';
		}
	}
	int get(int x, int y) { return arr[y - 1][x - 1].value; }
	int get_n(int x, int y) { return arr[y][x].n; }
};