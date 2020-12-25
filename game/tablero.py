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

	def liberar(self, x, y):
		pass

	def get_bandera(self, x, y):
		""" obtiene el estado del atributo bandera de una casilla en particular """
		return self.t[x][y].get_bandera()

	def get_visible(self, x, y):
		""" obtiene el estado del atributo 'visible' de una casilla en particular """
		return self.t[x][y].get_visible()

	def set_visible(self, x, y, estado):
		""" cambia el estado de visibilidad de una casilla en particular """
		self.t[x][y].set_visible(estado)

	def cambiar_bandera(self, x, y):
		""" si hay bandera en una casilla la quita y viceversa """
		self.t[x][y].set_bandera(not self.t[x][y].get_bandera())


