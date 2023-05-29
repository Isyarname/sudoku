#include "Sudoku_cells.h"
//#include <string>

void set(Sudoku& s, int x, int y, int value)
{
	bool res = s.set(x - 1, y - 1, value);
	if (!res)
		cout << "нельзя записать это значение ("<<value<<")!\n";
	cout << '\n';
}

int main()
{
	setlocale(LC_ALL, "ru");
    Sudoku s;
	int x, y;
	char value;
	int a, b, c;
	int temp;
    while (true)
    {
		cout << "x y value: ";
		cin >> x >> y >> value;

		if (value == 'r')  //записать строку
		{
			//temp = s.get(x, y);
			//if (temp == 0)
			//{
			cout << "x " << x << ' ' << x + 1 << ' ' << x + 2 << " : ";
			cin >> a >> b >> c;
			set(s, x, y, a);
			set(s, x + 1, y, b);
			set(s, x + 2, y, c);
			//}
			//else
			//	cout << "такие координаты уже заняты\n\n";
		}
		else if (value == 'p')
			s.print_potentials(x);
		else if (value == 't')
			s.print_potentials(x - 1, y - 1);
		else if (1<=value-'0' && value-'0' <= 9)
			set(s, x, y, value-'0');
		s.print();
    }
}

