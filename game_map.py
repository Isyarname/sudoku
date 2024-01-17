from map_settings import *
from classes import Square
import colors

__all__ = ['squares', 'selected_button', 'selected_button_coords', 'select_cell']

def _create_squares():
	sq = []
	for i in range(3):
		sq.append([])
		for j in range(3):
			coords = (i,j)
			sq[i].append(Square(i, j))
	return sq

def _create_list_of_cells(squares):
	cells = []

def select_button(pos):
	global selected_button
	global selected_button_coords
	for i, square_row in enumerate(squares):
		for j, square in enumerate(square_row):
			sf = square.form
			if (sf[0][0] <= pos[0] <= sf[2][0] and 
				sf[0][1] <= pos[1] <= sf[2][1]):
				ans = square.find_cell(pos)
				selected_button = ans["button"]
				selected_button_coords = [[i,j], ans["coords"]]
				return
	else:
		selected_button = False
		selected_button_coords = [[], []]

def caption():
	if inappropriate_value_mistake:
		return "mistake: inappropriate value set!"
	else:
		if get_theme() == "kitkat":
			return "kitkat theme"
		else:
			return str("Scheme:"+str(colors.get_scheme())+
				". Hue:"+str(colors.get_hue())+
				". Press S or H to change")

def update_forms():
	global squares
	new_squares = _create_squares()
	for i, square_row in enumerate(new_squares):
		for j, square in enumerate(square_row):
			squares[i][j].form = square.form
			for k, row in enumerate(square.cells):
				for l, cell in enumerate(row):
					squares[i][j].cells[k][l].value = cell.value
					squares[i][j].cells[k][l].digit_point = cell.digit_point
					for ii, pv in enumerate(squares[i][j].cells[k][l].possible_values):
						pv.form = cell.possible_values[ii].form

def get_squares():
	return squares

squares = _create_squares()
selected_button = False # Cell() | Poss_val()
inappropriate_value_mistake = False
selected_button_coords = [(0,0),[(0,0),(0,0)]]