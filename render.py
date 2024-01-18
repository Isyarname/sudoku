import pygame
import map_settings
import game_map
import colors

def _draw_text(surf, font, color, digit_point, value):
	text = font.render(str(value), True, color)
	place = text.get_rect(topleft=digit_point)
	surf.blit(text, place)

def _draw_button(surf, button, font, color, text_color, accent_color):
	pygame.draw.polygon(surf, color, button.form)
	if accent_color:
		x1, y1 = button.form[0]
		x2, y2 = button.form[1]
		accent_thickness = int((x2-x1)**0.5 * 2 / 7)
		point1, point2 = (x1+accent_thickness, y1), (x2-accent_thickness, y2)
		pygame.draw.line(surf, accent_color, point1, point2, accent_thickness)
	_draw_text(surf, font, text_color, button.digit_point, button.value)

def _draw_cell(surf, cell, cell_font, pv_font, clrs):
	if cell.value:
		_draw_button(surf, cell, cell_font, clrs["cell"], clrs["text"], clrs["cell_accent"])
	else:
		pygame.draw.polygon(surf, clrs["cell_background"], cell.form)
		for pv in cell.possible_values:
			_draw_button(surf, pv, pv_font, clrs["pv"], clrs["text"], clrs["pv_accent"])

def _draw_square(surf, square, cell_font, pv_font, clrs):
	pygame.draw.polygon(surf, clrs["square"], square.form)
	for row in square.cells:
		for cell in row:
			_draw_cell(surf, cell, cell_font, pv_font, clrs)

def draw(surf):
	clrs = colors.get()
	ms = map_settings.get()
	cell_font = pygame.font.SysFont(ms["font_name"], ms["cell_font_size"]) # cell
	pv_font = pygame.font.SysFont(ms["font_name"], ms["pv_font_size"]) # possible values
	surf.fill(clrs["background"])
	for row in game_map.get_squares():
		for square in row:
			_draw_square(surf, square, cell_font, pv_font, clrs)