from map_settings import *
import map_logic as ml

def remove(box_coords, cell_coords, val):
	remove_in_box(box_coords, val)
	remove_in_lines(box_coords, cell_coords, val)

def remove_in_box(box_coords, val):
	box = ml.boxes[box_coords[0]][box_coords[1]]
	for row in box.cells:
		for cell in row:
			cell.remove_value(val)

def remove_in_lines(box_coords, cell_coords, val):
	y = box_coords[0] * 3 + cell_coords[0]
	x = box_coords[1] * 3 + cell_coords[1]
	remove_in_row(y, val)
	remove_in_column(x, val)

def remove_in_row(y, val):
	for i in range(9):
		ml.matrix[y][i].remove_value(val)
		
def remove_in_column(x, val):
	for i in range(9):
		ml.matrix[i][x].remove_value(val)