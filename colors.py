import random as r
from map_settings import *
#schemes = [(4,2,3), (4,3,2), (1,3,2), (0,2,3), (1,2,3)]
# (0.7, 0.8, 1), (0.7, 1, 0.8), (0.6, 1, 0.8), (0.4, 0.8, 1), (0.6, 0.8, 1)
scheme_index = 0
hue = (0.8, 0.87, 1)
#shades = [0.4, 0.5, 0.6, 0.7, 0.8, 1]
schemes = [(0.7, 0.8, 1, 0.75), (0.7, 1, 0.8, 0.75), (0.6, 1, 0.8, 0.75), 
		  (0.4, 0.8, 1, 0.75), (0.6, 0.8, 1, 0.75)]
kitkat_colors = {"background":(23,26,30), "square":(23,26,30), "cell":(32,37,41), "cell_background":(18,21,24), "pv":(25,29,33), "text":(255,255,255)}
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
	if kitkat_theme:
		return kitkat_colors
	scheme = schemes[scheme_index] # shade scheme
	b = _dye(scheme[0])
	if indentations_from_edge_of_square:
		s = _dye(scheme[1])
	else:
		s = b
	c = _dye(scheme[2])
	cb = _dye(scheme[3])
	pv = _darken(c)
	t = (0,0,0)
	return {"background":b, "square":s, "cell":c, "cell_background":cb, "pv":pv, "text":t}