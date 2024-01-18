from map_settings import *
import game_map as gm

def set_by_click(coords):
	s_co = coords[0]
	c_co = coords[1][0]
	pv_co = coords[1][1]
	cell = gm.squares[s_co[0]][s_co[1]].cells[c_co[0]][c_co[1]]
	pv = cell.possible_values[pv_co]
	cell.value = pv.value
	remove_from_neighboring(s_co, c_co, cell.value)

def check_pv():
	while True:
		coords_lst = [] # cells with one possible value
		for i, square_row in enumerate(gm.squares):
			for j, square in enumerate(square_row):
				s_co = (i,j)
				c_coords = check_pv_in_square(square) # square.check_pv()
				for c_co in c_coords:
					coords_lst.append([s_co, c_co])
		if len(coords_lst) == 0:
			break
		else:
			for co in coords_lst:
				s_co, c_co = co
				set_last_pv(s_co, c_co)

def check_pv_in_square(square):
	lst = [] # cells with one possible value
	for i, row in enumerate(square.cells):
		for j, cell in enumerate(row):
			if (cell.value == 0 and 
				len(cell.possible_values) == 1):
				lst.append((i,j))
	return lst

def set_last_pv(s_co, c_co):
	cell = gm.squares[s_co[0]][s_co[1]].cells[c_co[0]][c_co[1]]
	if len(cell.possible_values) > 0:
		cell.value = cell.possible_values[0].value
		remove_from_neighboring(s_co, c_co, cell.value)
	else:
		gm.inappropriate_value_mistake = True

def remove_from_neighboring(s_co, c_co, val):
	remove_in_lines(s_co, c_co, val)
	remove_in_square(s_co, val)

def remove_in_lines(s_co, c_co, val):
	for i in range(3):
		gm.squares[s_co[0]][i].remove_in_row(c_co, val)
		gm.squares[i][s_co[1]].remove_in_column(c_co, val)

def remove_in_square(s_co, val):
	sq = gm.squares[s_co[0]][s_co[1]]
	for row in sq.cells:
		for cell in row:
			cell.remove_value(val)