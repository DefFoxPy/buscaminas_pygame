""" Funciones relacionadas para la gestión del tablero """

from .config import *
from .casilla import Casilla

class Tablero:

	def __init__(self):
		""" """
		self.t = list()
		self.crear()
		
	def crear(self):
		""" Agrega todas las casillas para el tablero 
		
		Recorre primero todas las columnas de una fila y luego para para la otra fila
		donde por cada columna va agregando una casilla
		"""
		for x in range(COLUMNA):
			self.t.append([])
			for y in range(FILA):
				casilla = Casilla(x, y)
				self.t[x].append(casilla)

	def mostrar(self, surface, dir_images):
		""" Muestra cada casilla dentro del tablero """
		for x in range(COLUMNA):
			for y in range(FILA):
				self.t[x][y].mostrar(surface, dir_images)

