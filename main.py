import pygame
import sys
from map_settings import *
import colors
import game_map as gm
import render
import sudoku_logic
from classes import *
clock = pygame.time.Clock()
pygame.init()

surface = pygame.display.set_mode((Width, Width))
c_font = pygame.font.SysFont(font_name, c_font_size) # cell
pv_font = pygame.font.SysFont(font_name, pv_font_size) # possible values

def quit():
	pygame.quit()
	sys.exit()

def draw():
	render.draw(surface, c_font, pv_font)
	pygame.display.set_caption(gm.caption())
	pygame.display.update()
	pygame.display.flip()


draw()
while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			gm.select_button(event.pos)
			if type(gm.selected_button) == Poss_val:
				sudoku_logic.set_by_click(gm.selected_button_coords)
			sudoku_logic.check_pv()
			draw()
		elif event.type == pygame.MOUSEBUTTONUP:
			pass
		elif event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit()
			elif event.key == pygame.K_s:
				colors.set_random_scheme()
				draw()
			elif event.key == pygame.K_h:
				colors.set_random_hue()
				draw()