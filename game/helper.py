import pygame

from .config import *

def cargar_imagen(direccion, transparente = True):
	""" Crea un objeto image dada la direccion y si tiene que se transparente o no """
	try: image = pygame.image.load(direccion)
	except pygame.error as message: raise SystemExit(message)

	image = image.convert()

	if transparente:
		color = image.get_at((0, 0))
		image.set_colorkey(color, pygame.RLEACCEL)

	return image
	
def pixeles_a_indice(pos):
	""" Convierte posicion de pixeles en forma de indices 

	Parámetros:
		pos(tuple): Representa la posicion del mouse en pixeles

	Returns:
		(x, y): la coordenada x, y 

	"""
	x = pos[0] // CASILLA_LARGO
	y = (pos[1] - MARGEN_Y) // CASILLA_ALTO

	return (x, y)

def coordenada_valida(x, y):
	""" determinar si una coordenada dada en x,y esta dentro de los limites del tablero """
	return (x >= 0 and x < COLUMNA) and (y >= 0 and y < FILA)

def display_text(surface, font_type, text, size, color, pos_x, pos_y):
	""" Muestra un texto en pantalla 
	
	Parámetros:
		surface: pantalla
		font_type(string): tipo de fuente
		text(string): mensaje a mostrar 
		size(int): tamaño de la letra
		color(int, int, int): color en formato RGB
		post_x(int): posicion en coordenada x
		post_y(int): posicion en coordenadas y 

	Returns:
		None
	"""
	font = pygame.font.Font(font_type, size)

	text = font.render(text, True, color)
	rect = text.get_rect()
	rect.midtop = (pos_x, pos_y)

	surface.blit(text, rect)