import pygame
import os

from .config import *
from .helper import *

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
		self.bandera = False
		self.pos_x = CASILLA_ALTO * x
		self.pos_y = CASILLA_LARGO * y + MARGEN_Y
		self.rect = [self.pos_x, self.pos_y, CASILLA_LARGO, CASILLA_ALTO]
		self.es_par = (x + y) % 2

	def get_bandera(self):
		return self.bandera

	def get_visible(self):
		return self.visible

	def set_bandera(self, estado):
		self.bandera = estado

	def set_visible(self, estado):
		self.visible = estado

	def mostrar(self, surface, dir_images):
		""" Dibuja la casilla """
		if not self.visible:
			if self.es_par:
				pygame.draw.rect(surface, COLOR_OCULTO_1, self.rect)
			else:
				pygame.draw.rect(surface, COLOR_OCULTO_2, self.rect)

			if self.bandera:
				imagen = cargar_imagen(os.path.join(dir_images, 'bandera.png'))
				surface.blit(imagen, [self.pos_x, self.pos_y])

		else:
			if self.es_par:
				pygame.draw.rect(surface, COLOR_EXPLORADO_1, self.rect)
			else:
				pygame.draw.rect(surface, COLOR_EXPLORADO_2, self.rect)
			
			if self.contenido != CASILLA_LIBRE:
				imagen = cargar_imagen(os.path.join(dir_images, IMAGENES[self.contenido]))
				surface.blit(imagen, [self.pos_x, self.pos_y])
