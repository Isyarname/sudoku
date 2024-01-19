from map_settings import *
import game_map as gm

def set_by_click(coords):
	box_coords = coords[0]
	cell_coords = coords[1][0]
	pvb_co = coords[1][1]
	cell = gm.boxes[box_coords[0]][box_coords[1]].cells[cell_coords[0]][cell_coords[1]]
	pvb = cell.possible_value_buttons[pvb_co]
	cell.value = pvb.value
	remove_from_neighboring(box_coords, cell_coords, cell.value)

def check_pvs():
	while True:
		coords_lst = [] # cells with one possible value
		for i, box_row in enumerate(gm.boxes):
			for j, box in enumerate(box_row):
				box_coords = (i,j)
				cell_coords = check_pvs_in_box(box)
				for cell_coords in cell_coords:
					coords_lst.append([box_coords, cell_coords])
		if len(coords_lst) == 0:
			break
		else:
			for co in coords_lst:
				box_coords, cell_coords = co
				set_last_pv(box_coords, cell_coords)

def check_pvs_in_box(box):
	lst = [] # cells with one possible value
	for i, row in enumerate(box.cells):
		for j, cell in enumerate(row):
			if (cell.value == 0 and 
				len(cell.possible_value_buttons) == 1):
				lst.append((i,j))
	return lst

def set_last_pv(box_coords, cell_coords):
	cell = gm.boxes[box_coords[0]][box_coords[1]].cells[cell_coords[0]][cell_coords[1]]
	if len(cell.possible_value_buttons) > 0:
		cell.value = cell.possible_value_buttons[0].value
		remove_from_neighboring(box_coords, cell_coords, cell.value)
	else:
		gm.inappropriate_value_mistake = True

def remove_from_neighboring(box_coords, cell_coords, val):
	remove_in_lines(box_coords, cell_coords, val)
	remove_in_box(box_coords, val)

def remove_in_lines(box_coords, cell_coords, val):
	for i in range(3):
		gm.boxes[box_coords[0]][i].remove_in_row(cell_coords, val)
		gm.boxes[i][box_coords[1]].remove_in_column(cell_coords, val)

def remove_in_box(box_coords, val):
	sq = gm.boxes[box_coords[0]][box_coords[1]]
	for row in sq.cells:
		for cell in row:
			cell.remove_value(val)