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

def _create_possible_value_buttons(x, y, pvb_td, font_name, pvb_width):
	pvb = []
	for i in range(9):
		c1 = i % 3
		c2 = i // 3
		x1, y1 = x + pvb_td*c1, y + pvb_td*c2
		form = _create_form(x1,y1,pvb_width)
		digit_point = _create_digit_point(x1, y1, pvb_width, font_name)
		pvb.append(Possible_value_button(form, digit_point, value=i+1))
	return pvb

def _create_cells(x, y, cell_td, cell_width, font_name, pvb_td, pvb_width):
	cells = []
	for i in range(3):
		cells.append([])
		for j in range(3):
			x1, y1 = x+cell_td*j, y+cell_td*i
			form = _create_form(x1, y1, cell_width)
			digit_point = _create_digit_point(x1, y1, cell_width, font_name)
			possible_value_buttons = _create_possible_value_buttons(x1, y1, pvb_td, font_name, pvb_width)
			cells[i].append(Cell(form, digit_point, possible_value_buttons, value=0))
	return cells

def _create_boxes():
	sq = []
	d = map_settings.get()
	boxes_gap = d["boxes_gap"]
	cells_gap = d["cells_gap"]
	box_td = d["box_td"]
	cell_td = d["cell_td"]
	box_width = d["box_width"]
	cell_width = d["cell_width"]
	font_name = d["font_name"]
	pvb_width = d["pvb_width"]
	pvb_td = d["pvb_td"]
	for i in range(3):
		sq.append([])
		for j in range(3):
			coords = (i,j)
			x = boxes_gap + box_td*j
			y = boxes_gap + box_td*i
			form = _create_form(x,y,box_width)
			if d["indentations_from_edge_of_box"]:
				cells = _create_cells(x+cells_gap, y+cells_gap, cell_td, cell_width, font_name, pvb_td, pvb_width)
			else:
				cells = _create_cells(x, y, cell_td, cell_width, font_name, pvb_td, pvb_width)
			sq[i].append(Box(form, cells))
	return sq

def select_button(pos):
	global selected_button
	global selected_button_coords
	for i, box_row in enumerate(boxes):
		for j, box in enumerate(box_row):
			sf = box.form
			if (sf[0][0] <= pos[0] <= sf[2][0] and 
				sf[0][1] <= pos[1] <= sf[2][1]):
				ans = box.find_cell(pos)
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
	global boxes
	new_boxes = _create_boxes()
	for i, box_row in enumerate(new_boxes):
		for j, box in enumerate(box_row):
			boxes[i][j].form = box.form
			for k, row in enumerate(box.cells):
				for l, cell in enumerate(row):
					boxes[i][j].cells[k][l].value = cell.value
					boxes[i][j].cells[k][l].digit_point = cell.digit_point
					for ii, pvb in enumerate(boxes[i][j].cells[k][l].possible_value_buttons):
						pvb.form = cell.possible_value_buttons[ii].form

def get_boxes():
	return boxes

boxes = _create_boxes()
selected_button = False # Cell() | Possible_value_button()
pressed_button = False # Possible_value_button()
inappropriate_value_mistake = False
selected_button_coords = [(0,0),[(0,0),(0,0)]]