import map_settings
from classes import *
import colors

def _create_form(x, y, width):
	return ((x, y), (x+width, y), (x+width, y+width), (x, y+width))

def _create_digit_point(x, y, width, font_name):
	if font_name == "roboto":
		return (x+width*0.33, y+width*0.22)
	elif font_name == "arial":
		return (x+width*0.3, y)

def _create_possible_values(x, y, pvtd, font_name, pv_width):
	pv = []
	for i in range(9):
		c1 = i % 3
		c2 = i // 3
		x1, y1 = x + pvtd*c1, y + pvtd*c2
		form = _create_form(x1,y1,pv_width)
		digit_point = _create_digit_point(x1, y1, pv_width, font_name)
		pv.append(Poss_val(form, digit_point, value=i+1))
	return pv

def _create_cells(x, y, ctd, c_width, font_name, pvtd, pv_width):
	cells = []
	for i in range(3):
		cells.append([])
		for j in range(3):
			x1, y1 = x+ctd*j, y+ctd*i
			form = _create_form(x1, y1, c_width)
			digit_point = _create_digit_point(x1, y1, c_width, font_name)
			possible_values = _create_possible_values(x1, y1, pvtd, font_name, pv_width)
			cells[i].append(Cell(form, digit_point, possible_values, value=0))
	return cells

def _create_squares():
	sq = []
	d = map_settings.get()
	s_gap = d["s_gap"]
	c_gap = d["c_gap"]
	std = d["std"]
	ctd = d["ctd"]
	s_width = d["s_width"]
	c_width = d["c_width"]
	font_name = d["font_name"]
	pv_width = d["pv_width"]
	pvtd = d["pvtd"]
	for i in range(3):
		sq.append([])
		for j in range(3):
			coords = (i,j)
			x = s_gap + std*j
			y = s_gap + std*i
			form = _create_form(x,y,s_width)
			if d["indentations_from_edge_of_square"]:
				cells = _create_cells(x+c_gap, y+c_gap, ctd, c_width, font_name, pvtd, pv_width)
			else:
				cells = _create_cells(x, y, ctd, c_width, font_name, pvtd, pv_width)
			sq[i].append(Square(form, cells))
	return sq

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
		if map_settings.get()["theme"] == "kitkat":
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