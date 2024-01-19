import pygame
import sys
import map_settings
import colors
import game_map as gm
import render
import sudoku_logic
from classes import *
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.init()
surface = pygame.display.set_mode((map_settings.Width, map_settings.Width))
digit_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, 
			pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
try:
	pygame.mixer.music.load("HARD DRIVE.mp3")
	pygame.mixer.music.queue("009 Sound System - Dreamscape.mp3")
	pygame.mixer.music.play()
	music_loaded = True
except:
	music_loaded = False

def quit():
	pygame.quit()
	sys.exit()

def draw():
	render.draw(surface)
	pygame.display.set_caption(gm.caption())
	pygame.display.update()
	pygame.display.flip()


draw()
while True:
	if gm.pressed_button:
		gm.select_button(pygame.mouse.get_pos())
		if gm.selected_button != gm.pressed_button:
			gm.pressed_button.is_pressed = False
			gm.pressed_button = False
			draw()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			gm.select_button(event.pos)
			if type(gm.selected_button) == Possible_value_button:
				gm.pressed_button = gm.selected_button
				gm.selected_button.is_pressed = True
				draw()
		elif event.type == pygame.MOUSEBUTTONUP:
			gm.select_button(event.pos)
			if gm.pressed_button and gm.selected_button == gm.pressed_button:
				sudoku_logic.set_by_click(gm.selected_button_coords)
				sudoku_logic.check_pvs()
				gm.pressed_button.is_pressed = False
				gm.pressed_button = False
				draw()
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
			elif event.key == pygame.K_t:
				map_settings.change_theme()
				draw()
			elif event.key in digit_keys and music_loaded:
				vol = digit_keys.index(event.key) / 9
				pygame.mixer.music.set_volume(vol)