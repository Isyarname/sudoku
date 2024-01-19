import random as r
import map_settings

scheme_index = 0
hue = (0.8, 0.87, 1)
schemes = [(0.7, 0.8, 1, 0.75), (0.7, 1, 0.8, 0.75), (0.6, 1, 0.8, 0.75),                                        # pvb    25,29,33
		  (0.4, 0.8, 1, 0.75), (0.6, 0.8, 1, 0.75)]
kitkat_colors = {"background":(6,7,8), "box":(6,7,8), "cell":(32,37,41), "cell_background":(14,16,18), 
"pvb":(23,26.5,29.5), "text":(255,255,255), "cell_accent":(64,69,73), "pvb_accent":(43.5,47.5,50.5),
"pressed_button":(25,79,99), "pressed_accent":(9,125,164)}


def get_hue():
	return (round(hue[0], 2), round(hue[1], 2), round(hue[2], 2))
def get_scheme():
	return schemes[scheme_index]
def set_random_scheme():
	global scheme_index
	scheme_index = r.randint(0, len(schemes)-1)
def set_random_hue():
	global hue
	minV = 0.8
	hue = (r.uniform(minV, 1), r.uniform(minV, 1), r.uniform(minV, 1))
def _darken(color, k=0.93):
	return (color[0]*k,
			color[1]*k,
			color[2]*k)
def _dye(shade):
	return (shade*hue[0]*255,
			shade*hue[1]*255,
			shade*hue[2]*255)
def get():
	settings = map_settings.get()
	if settings["theme"] == "kitkat":
		return kitkat_colors
	scheme = schemes[scheme_index] # shade scheme
	background = _dye(scheme[0])
	if settings["indentations_from_edge_of_box"]:
		box = _dye(scheme[1])
	else:
		box = background
	cell = _dye(scheme[2])
	cell_background = _dye(scheme[3])
	pvb = _darken(cell)
	text = (0,0,0)
	return {"background":background, "box":box, "cell":cell, 
	"cell_background":cell_background, "pvb":pvb, "text":text,
	"cell_accent":False, "pvb_accent":False,
	"pressed_button":False, "pressed_accent":False}