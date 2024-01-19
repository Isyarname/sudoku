def change_theme():
	global kitkat_theme
	kitkat_theme = not kitkat_theme
	_set()

def _set():
	global font_name, indentations_from_edge_of_box, boxes_gap, cells_gap, pvb_gap
	global box_width, cell_width, pvb_width, box_td, cell_td, pvb_td, cell_font_size, pvb_font_size
	if kitkat_theme:
		font_name = "roboto"
		indentations_from_edge_of_box = 0
		boxes_gap = 10 # gap between boxes 3*3
		cells_gap = 5 # gap between cells
		pvb_gap = 2 # gap between possible values in cell
	else:
		font_name = "arial"
		indentations_from_edge_of_box = 1
		boxes_gap = 6 # gap between boxes 3*3
		cells_gap = 4 # gap between cells
		pvb_gap = 2 # gap between possible values in cell

	box_width = (Width - boxes_gap * 4) / 3
	if indentations_from_edge_of_box:
		cell_width = (box_width - cells_gap * 4) / 3
	else:
		cell_width = (box_width - cells_gap * 2) / 3
	pvb_width = (cell_width - pvb_gap * 2) / 3

	box_td = box_width + boxes_gap # box translation distance
	cell_td = cell_width + cells_gap # cell translation distance
	pvb_td = pvb_width + pvb_gap # possible value translation distance

	if font_name == "roboto":
		cell_font_size = int(cell_width)
		pvb_font_size = cell_font_size // 3
	elif font_name == "arial":
		cell_font_size = int(cell_width / 1.1)
		pvb_font_size = int(cell_font_size / 3.1)

def get():
	if kitkat_theme:
		theme = "kitkat"
	else:
		theme = "default"
	return {
		"Width":Width,
		"theme":theme,
		"font_name":font_name,
		"indentations_from_edge_of_box":indentations_from_edge_of_box,
		"boxes_gap":boxes_gap,
		"cells_gap":cells_gap,
		"pvb_gap":pvb_gap,
		"box_width":box_width,
		"cell_width":cell_width,
		"pvb_width":pvb_width,
		"box_td":box_td,
		"cell_td":cell_td,
		"pvb_td":pvb_td,
		"cell_font_size":cell_font_size,
		"pvb_font_size":pvb_font_size
		}

Width = 750
kitkat_theme = True
_set()