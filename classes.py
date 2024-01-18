import map_settings

class Poss_val:
	def __init__(self, form, digit_point, value):
		self.value = value
		self.form = form
		self.digit_point = digit_point

class Cell:
	def __init__(self, form, digit_point, possible_values, value=0):
		self.form = form
		self.digit_point = digit_point
		self.possible_values = possible_values
		self.value = value
	def remove_value(self, val):
		if self.value == 0:
			for pv in self.possible_values:
				if pv.value == val:
					self.possible_values.remove(pv)
					break
	def find_pv(self, pos):
		for i, pv in enumerate(self.possible_values):
			pvf = pv.form
			if (pvf[0][0] <= pos[0] <= pvf[2][0] and 
				pvf[0][1] <= pos[1] <= pvf[2][1]):
				return {"button":pv, "coords":i}
		else:
			return {"button":False, "coords":False}

class Square:
	def __init__(self, form, cells):
		self.form = form
		self.cells = cells
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
		for i in range(3):
			self.cells[x][i].remove_value(val)
	def remove_in_column(self, c_coords, val):
		x, y = c_coords
		for i in range(3):
			self.cells[i][y].remove_value(val)