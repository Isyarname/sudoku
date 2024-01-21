import pygame
import map_settings
import map_logic
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

def _draw_pressed_button(surf, button, font, color, text_color, accent_color=0):
	pygame.draw.polygon(surf, color, button.form)
	if accent_color:
		accent_thickness = 2
		for i in range(4):
			pygame.draw.line(surf, accent_color, button.form[i], button.form[(i+1)%4], accent_thickness)
	_draw_text(surf, font, text_color, button.digit_point, button.value)

def _draw_cell(surf, cell, cell_font, pvb_font, clrs):
	if cell.value:
		_draw_button(surf, cell, cell_font, clrs["cell"], clrs["text"], clrs["cell_accent"])
	else:
		pygame.draw.polygon(surf, clrs["cell_background"], cell.form)
		for pvb in cell.possible_value_buttons:
			if pvb.is_pressed and clrs["pressed_button"]:
				_draw_pressed_button(surf, pvb, pvb_font, clrs["pressed_button"], clrs["text"], clrs["pressed_accent"])
			else:
				_draw_button(surf, pvb, pvb_font, clrs["pvb"], clrs["text"], clrs["pvb_accent"])

def _draw_box(surf, box, cell_font, pvb_font, clrs):
	pygame.draw.polygon(surf, clrs["box"], box.form)
	for row in box.cells:
		for cell in row:
			_draw_cell(surf, cell, cell_font, pvb_font, clrs)

def draw(surf):
	clrs = colors.get()
	ms = map_settings.get()
	cell_font = pygame.font.SysFont(ms["font_name"], ms["cell_font_size"]) # cell
	pvb_font = pygame.font.SysFont(ms["font_name"], ms["pvb_font_size"]) # possible values
	surf.fill(clrs["background"])
	for row in map_logic.get_boxes():
		for box in row:
			_draw_box(surf, box, cell_font, pvb_font, clrs)