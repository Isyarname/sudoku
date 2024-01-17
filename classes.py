from map_settings import *

__all__ = ["Poss_val", "Cell", "Square"]

def _create_form(x, y, width):
	return ((x, y), (x+width, y), (x+width, y+width), (x, y+width))
def _create_digit_point(x, y, width):
	if font_name == "roboto":
		return (x+width*0.33, y+width*0.22)
	elif font_name == "arial":
		return (x+width*0.3, y)
def _create_cells(x, y):
	cells = []
	for i in range(3):
		cells.append([])
		for j in range(3):
			x1, y1 = x+ctd*j, y+ctd*i
			cells[i].append(Cell(x1, y1))
	return cells
def _create_possible_values(x, y):
	pv = []
	for i in range(9):
		c1 = i % 3
		c2 = i // 3
		x1, y1 = x + pvtd*c1, y + pvtd*c2
		pv.append(Poss_val(x1, y1, value=i+1))
	return pv


class Poss_val:
	def __init__(self, x, y, value):
		self.value = value
		self.form = _create_form(x,y,pv_width)
		self.digit_point = _create_digit_point(x, y, pv_width)


class Cell:
	def __init__(self, x, y):
		self.value = 0
		self.possible_values = _create_possible_values(x,y)
		self.form = _create_form(x,y,c_width)
		self.digit_point = _create_digit_point(x, y, c_width)
	def remove_value(self, val):
		if self.value == 0:
			for pv in self.possible_values:
				if pv.value == val:
					self.possible_values.remove(pv)
					break
			'''if len(self.possible_values) == 1:
				self.value = self.possible_values[0].value
				return True
		return False'''
	def find_pv(self, pos):
		for i, pv in enumerate(self.possible_values):
			pvf = pv.form
			if (pvf[0][0] <= pos[0] <= pvf[2][0] and 
				pvf[0][1] <= pos[1] <= pvf[2][1]):
				return {"button":pv, "coords":i}
		else:
			return {"button":False, "coords":False}


class Square:
	def __init__(self, i, j):
		x = s_gap + std*j
		y = s_gap + std*i
		self.form = _create_form(x,y,s_width)
		if indentations_from_edge_of_square:
			self.cells = _create_cells(x+c_gap, y+c_gap)
		else:
			self.cells = _create_cells(x, y)
	def find_cell(self, pos):
		for i, row in enumerate(self.cells):
			for j, cell in enumerate(row):
				cf = cell.form
				if (cf[0][0] <= pos[0] <= cf[2][0] and 
					cf[0][1] <= pos[1] <= cf[2][1]):
					if cell.value == 0:
						ans = cell.find_pv(pos)
						return {"button":ans["button"], "coords":[[i,j],ans["coords"]]}
					else:
						return {"button":cell, "coords":[i,j]}
		else:
			return {"button":False, "coords":[]}
	def remove_in_row(self, c_coords, val):
		x, y = c_coords
		set_cells = []
		for i in range(3):
			self.cells[x][i].remove_value(val)
	def remove_in_column(self, c_coords, val):
		x, y = c_coords
		for i in range(3):
			self.cells[i][y].remove_value(val)
	'''def check_pv(self):
		lst = [] # cells with one possible value
		for i, row in enumerate(self.cells):
			for j, cell in enumerate(row):
				if (cell.value == 0 and 
					len(cell.possible_values) == 1):
					lst.append((i,j))
		return lst'''