import pygame
from map_settings import *
from game_map import squares
import colors


def _draw_button(b, surf, font, b_color, clrs, line_thickness=2):
	pygame.draw.polygon(surf, b_color, b.form)
	if kitkat_theme:
		x1, y1 = b.form[0][0], b.form[0][1]
		x2, y2 = b.form[1][0], b.form[1][1]
		pygame.draw.line(surf, (64,69,73), (x1+line_thickness, y1), (x2 - line_thickness, y2), line_thickness)
	text = font.render(str(b.value), True, clrs["text"])
	place = text.get_rect(topleft=b.digit_point)
	surf.blit(text, place)
def _draw_cell(cell, surf, c_font, pv_font, clrs):
	if cell.value != 0:
		_draw_button(cell, surf, c_font, clrs["cell"], clrs)
	else:
		pygame.draw.polygon(surf, clrs["cell_background"], cell.form)
		for pv in cell.possible_values:
			_draw_button(pv, surf, pv_font, clrs["pv"], clrs, 1)
def _draw_square(square, surf, c_font, pv_font, clrs):
	pygame.draw.polygon(surf, clrs["square"], square.form)
	for row in square.cells:
		for cell in row:
			_draw_cell(cell, surf, c_font, pv_font, clrs)
def draw(surf, c_font, pv_font):
	clrs = colors.get()
	surf.fill(clrs["background"])
	for row in squares:
		for square in row:
			_draw_square(square, surf, c_font, pv_font, clrs)