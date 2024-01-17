Width = 750
c_gap = 5 # gap between cells
pv_gap = 2 # gap between possible values in cell



kitkat_theme = 1



if kitkat_theme:
	indentations_from_edge_of_square = 0
	s_gap = 7 # gap between squares 3*3
	text_color = (255,255,255)
	font_name = "roboto"
else:
	indentations_from_edge_of_square = 1
	s_gap = 7 # gap between squares 3*3
	text_color = (0,0,0)
	font_name = "arial"

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