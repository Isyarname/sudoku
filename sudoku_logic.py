from map_settings import *
import map_logic as ml
import remove_from_blocks
#import last_place_in_block
#import threesomes

def set_by_click(coords):
	box_coords = coords[0]
	cell_coords = coords[1][0]
	pvb_co = coords[1][1]
	cell = ml.boxes[box_coords[0]][box_coords[1]].cells[cell_coords[0]][cell_coords[1]]
	pvb = cell.possible_value_buttons[pvb_co]
	cell.value = pvb.value
	remove_from_blocks.remove(box_coords, cell_coords, cell.value)

def check():
	check_pvs()
	#threesomes.remove()


def check_pvs():
	while True:
		coords_lst = [] # cells with one possible value
		for i, box_row in enumerate(ml.boxes):
			for j, box in enumerate(box_row):
				cell_coords = check_pvs_in_box(box)
				for cell_coords in cell_coords:
					coords_lst.append([(i,j), cell_coords])
		if len(coords_lst) == 0:
			break
		else:
			for coords in coords_lst:
				set_last_pv(*coords)

def check_pvs_in_box(box):
	lst = [] # cells with one possible value
	for i, row in enumerate(box.cells):
		for j, cell in enumerate(row):
			if (cell.value == 0 and 
				len(cell.possible_value_buttons) == 1):
				lst.append((i,j))
	return lst

def set_last_pv(box_coords, cell_coords):
	cell = ml.boxes[box_coords[0]][box_coords[1]].cells[cell_coords[0]][cell_coords[1]]
	if len(cell.possible_value_buttons) > 0:
		cell.value = cell.possible_value_buttons[0].value
		remove_from_blocks.remove(box_coords, cell_coords, cell.value)
	else:
		ml.inappropriate_value_mistake = True

