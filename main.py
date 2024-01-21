import pygame
import os
import sys
import random
import map_settings
import colors
import map_logic as ml
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
	pygame.mixer.music.load("./sound/music/HARD DRIVE.mp3")
	pygame.mixer.music.queue("./sound/music/009 Sound System - Dreamscape.mp3")
	pygame.mixer.music.play()
	pygame.mixer.music.set_volume(0.1)
	music_loaded = True
	mistake_sound_played = False
except:
	music_loaded = False

try:
	button_down_sound = pygame.mixer.Sound("./sound/click/Join.mp3")
	button_up_sound = pygame.mixer.Sound("./sound/click/Leave.mp3")
	mistake_sound_names = os.listdir("./sound/mistake")
	mistake_sounds = [pygame.mixer.Sound("./sound/mistake/"+file_name) for file_name in mistake_sound_names]
	value_set_sound_names = os.listdir("./sound/value_set")
	value_set_sounds = [pygame.mixer.Sound("./sound/value_set/"+file_name) for file_name in value_set_sound_names]
	sounds_loaded = True
except:
	sounds_loaded = False

def quit():
	pygame.quit()
	sys.exit()

def draw():
	render.draw(surface)
	pygame.display.set_caption(ml.caption())
	pygame.display.update()
	pygame.display.flip()


draw()
while True:
	if ml.pressed_button:
		ml.select_button(pygame.mouse.get_pos())
		if ml.selected_button != ml.pressed_button:
			ml.pressed_button.is_pressed = False
			ml.pressed_button = False
			if sounds_loaded:
				button_up_sound.play()
			draw()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			ml.select_button(event.pos)
			if type(ml.selected_button) == Possible_value_button:
				ml.pressed_button = ml.selected_button
				ml.selected_button.is_pressed = True
				if sounds_loaded:
					button_down_sound.play()
				draw()
		elif event.type == pygame.MOUSEBUTTONUP:
			ml.select_button(event.pos)
			if ml.pressed_button and ml.selected_button == ml.pressed_button:
				sudoku_logic.set_by_click(ml.selected_button_coords)
				sudoku_logic.check()
				if sounds_loaded:
					if ml.inappropriate_value_mistake and not mistake_sound_played:
						random.choice(mistake_sounds).play()
						mistake_sound_played = True
					else:
						random.choice(value_set_sounds).play()
				ml.pressed_button.is_pressed = False
				ml.pressed_button = False
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