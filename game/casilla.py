import pygame

from .config import *

def casilla_valida(x, y):
	""" Determina si la coordenda y, x de una casilla es valida """
	es_valido = (x >= 0 and  x < COLUMNA) and (y >= 0 and y < FILA)
	return es_valido

class Casilla:

	def __init__(self, x, y):
		""" Creacion de la casilla
		Por defecto:
		  * la casilla no muestra su contenido
		  * la casilla no tiene nada, es decír está libre

		convierte la posición relativa del tablero de la casilla [i,j] a su
		equivalente en pixeles. Ejemplo [1, 2] -> x = 80, y = 95
		"""
		self.visible = False  
		self.contenido = CASILLA_LIBRE
		self.pos_x = CASILLA_ALTO * x
		self.pos_y = CASILLA_LARGO * y + MARGEN_Y
		self.rect = [self.pos_x, self.pos_y, CASILLA_LARGO, CASILLA_ALTO]
		self.es_par = (x + y) % 2

	def mostrar(self, surface):
		""" Dibuja la casilla """
		if not self.visible:
			if self.es_par:
				pygame.draw.rect(surface, COLOR_OCULTO_1, self.rect)
			else:
				pygame.draw.rect(surface, COLOR_OCULTO_2, self.rect)
		else:
			# TO DO: mostrar imagen
			pass
