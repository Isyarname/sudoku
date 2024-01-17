def change_theme():
	global kitkat_theme
	kitkat_theme = not kitkat_theme
	_set_theme()

def _set_theme():
	global font_name, indentations_from_edge_of_square, s_gap, c_gap, pv_gap
	global s_width, c_width, pv_width, std, ctd, pvtd, c_font_size, pv_font_size
	if kitkat_theme:
		font_name = "roboto"
		indentations_from_edge_of_square = 0
		s_gap = 10 # gap between squares 3*3
		c_gap = 5 # gap between cells
		pv_gap = 2 # gap between possible values in cell
	else:
		font_name = "arial"
		indentations_from_edge_of_square = 1
		s_gap = 6 # gap between squares 3*3
		c_gap = 4 # gap between cells
		pv_gap = 2 # gap between possible values in cell

	s_width = (Width - s_gap * 4) / 3
	if indentations_from_edge_of_square:
		c_width = (s_width - c_gap * 4) / 3
	else:
		c_width = (s_width - c_gap * 2) / 3
	pv_width = (c_width - pv_gap * 2) / 3

	std = s_width + s_gap # square translation distance
	ctd = c_width + c_gap # cell translation distance
	pvtd = pv_width + pv_gap # possible value translation distance

	if font_name == "roboto":
		c_font_size = int(c_width)
		pv_font_size = c_font_size // 3
	elif font_name == "arial":
		c_font_size = int(c_width / 1.1)
		pv_font_size = int(c_font_size / 3.1)

def get_theme():
	if kitkat_theme:
		return "kitkat"
	else:
		return "default"

def get_fonts():
	return {"font_name":font_name, "c_font_size":c_font_size, "pv_font_size":pv_font_size}

def get_indentations():
	return indentations_from_edge_of_square

def get_dict():
	return {
		"Width":Width,
		"kitkat_theme":kitkat_theme,
		"font_name":font_name,
		"indentations_from_edge_of_square":indentations_from_edge_of_square,
		"s_gap":s_gap,
		"c_gap":c_gap,
		"pv_gap":pv_gap,
		"s_width":s_width,
		"c_width":c_width,
		"pv_width":pv_width,
		"std":std,
		"ctd":ctd,
		"pvtd":pvtd,
		"c_font_size":c_font_size,
		"pv_font_size":pv_font_size
		}

Width = 750
kitkat_theme = 0
_set_theme()