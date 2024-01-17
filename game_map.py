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
		return str("Scheme:"+str(colors.get_scheme())+
				". Hue:"+str(colors.get_hue())+
				". Press S or H to change")

squares = _create_squares()
selected_button = False # Cell() | Poss_val()
inappropriate_value_mistake = False
selected_button_coords = [(0,0),[(0,0),(0,0)]]