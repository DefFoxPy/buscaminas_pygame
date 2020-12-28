import pygame

from .config import *

def cargar_imagen(direccion, transparente = True):
	try: image = pygame.image.load(direccion)
	except pygame.error as message: raise SystemExit(message)

	image = image.convert()

	if transparente:
		color = image.get_at((0, 0))
		image.set_colorkey(color, pygame.RLEACCEL)

	return image
	
def pixeles_a_indice(pos):
	""" Convierte posicion de pixeles en forma de indices """
	x = pos[0] // CASILLA_LARGO
	y = (pos[1] - MARGEN_Y) // CASILLA_ALTO

	return (x, y)

def coordenada_valida(x, y):
	""" determinar si una coordenada dada en x,y esta dentro de los limites del tablero """
	return (x >= 0 and x < COLUMNA) and (y >= 0 and y < FILA)

def display_text(surface, font_type, text, size, color, pos_x, pos_y):
	font = pygame.font.Font(font_type, size)

	text = font.render(text, True, color)
	rect = text.get_rect()
	rect.midtop = (pos_x, pos_y)

	surface.blit(text, rect)