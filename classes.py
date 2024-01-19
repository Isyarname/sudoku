import map_settings

class Possible_value_button:
	def __init__(self, form, digit_point, value):
		self.value = value
		self.form = form
		self.digit_point = digit_point
		self.is_pressed = False

class Cell:
	def __init__(self, form, digit_point, possible_value_buttons, value=0):
		self.form = form
		self.digit_point = digit_point
		self.possible_value_buttons = possible_value_buttons
		self.value = value
	def remove_value(self, val):
		if self.value == 0:
			for pvb in self.possible_value_buttons:
				if pvb.value == val:
					self.possible_value_buttons.remove(pvb)
					break
	def get_values(self):
		values = []
		for pvb in self.possible_value_buttons:
			values.append(pvb.value)
		return values.sorted()
	def find_pvb(self, pos):
		for i, pvb in enumerate(self.possible_value_buttons):
			pvbf = pvb.form
			if (pvbf[0][0] <= pos[0] <= pvbf[2][0] and 
				pvbf[0][1] <= pos[1] <= pvbf[2][1]):
				return {"button":pvb, "coords":i}
		else:
			return {"button":False, "coords":False}

class Box:
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
						ans = cell.find_pvb(pos)
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