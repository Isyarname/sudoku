import pygame
import map_settings
from game_map import get_squares
from classes import Cell, Poss_val
import colors


def _draw_button(b, surf, font, clrs):
	if type(b) == Cell:
		b_color = clrs["cell"]
		line_thickness = 2
	elif type(b) == Poss_val:
		b_color = clrs["pv"]
		line_thickness = 1
	pygame.draw.polygon(surf, b_color, b.form)
	if map_settings.get_theme() == "kitkat":
		if type(b) == Cell:
			accent_color = clrs["cell_accent"]
		elif type(b) == Poss_val:
			accent_color = clrs["pv_accent"]
		x1, y1 = b.form[0][0], b.form[0][1]
		x2, y2 = b.form[1][0], b.form[1][1]
		pygame.draw.line(surf, accent_color, (x1+line_thickness, y1), (x2 - line_thickness, y2), line_thickness)
	text = font.render(str(b.value), True, clrs["text"])
	place = text.get_rect(topleft=b.digit_point)
	surf.blit(text, place)
def _draw_cell(cell, surf, c_font, pv_font, clrs):
	if cell.value != 0:
		_draw_button(cell, surf, c_font, clrs)
	else:
		pygame.draw.polygon(surf, clrs["cell_background"], cell.form)
		for pv in cell.possible_values:
			_draw_button(pv, surf, pv_font, clrs)
def _draw_square(square, surf, c_font, pv_font, clrs):
	pygame.draw.polygon(surf, clrs["square"], square.form)
	for row in square.cells:
		for cell in row:
			_draw_cell(cell, surf, c_font, pv_font, clrs)
def draw(surf):
	clrs = colors.get()
	f = map_settings.get_fonts()
	font_name, c_font_size, pv_font_size = f["font_name"], f["c_font_size"], f["pv_font_size"]
	c_font = pygame.font.SysFont(font_name, c_font_size) # cell
	pv_font = pygame.font.SysFont(font_name, pv_font_size) # possible values
	surf.fill(clrs["background"])
	squares = get_squares()
	for row in squares:
		for square in row:
			_draw_square(square, surf, c_font, pv_font, clrs)