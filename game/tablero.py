""" Funciones relacionadas para la gestión del tablero """

from .config import *
from .casilla import Casilla
from .helper import *

class Tablero:

	def __init__(self):
		""" """
		self.t = list()
		self.crear()
		self.agregar_minas()
		self.agregar_numeros()
		
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

	def agregar_minas(self):
		""" por ahora agrega 10 minas de manera aleatorea """
		from random import randint

		minas_agregadas = 0

		while minas_agregadas < NUMERO_MINAS:
			x = randint(0, COLUMNA-1)
			y = randint(0, FILA-1)

			if self.t[x][y].get_contenido() != CASILLA_MINA:
				self.t[x][y].set_contenido(CASILLA_MINA)
				minas_agregadas += 1

	def agregar_numeros(self):
		""" """
		for x in range(COLUMNA):
			for y in range(FILA):
				
				if self.t[x][y].get_contenido() == CASILLA_MINA: continue
				numero_minas = 0

				if coordenada_valida(x-1, y-1) and self.t[x-1][y-1].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				if coordenada_valida(x, y-1) and self.t[x][y-1].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				if coordenada_valida(x+1, y-1) and self.t[x+1][y-1].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				if coordenada_valida(x-1, y) and self.t[x-1][y].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				if coordenada_valida(x+1, y) and self.t[x+1][y].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				if coordenada_valida(x-1, y+1) and self.t[x-1][y+1].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				if coordenada_valida(x, y+1) and self.t[x][y+1].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				if coordenada_valida(x+1, y+1) and self.t[x+1][y+1].get_contenido() == CASILLA_MINA:
					numero_minas += 1

				self.t[x][y].set_contenido(numero_minas)

	def liberar(self, x, y):
		""" """
		# Casos bases
		if not coordenada_valida(x, y): return
		if self.t[x][y].get_visible(): return
		if self.t[x][y].get_contenido() == CASILLA_MINA: return

		if self.t[x][y].get_contenido() not in [CASILLA_LIBRE, CASILLA_MINA]: # Número
			self.t[x][y].set_visible(True)
			return 

		if self.t[x][y].get_contenido() == CASILLA_LIBRE:
			self.t[x][y].set_visible(True)

		# Caso recursivo
		self.liberar(x-1, y)
		self.liberar(x-1, y-1)
		self.liberar(x, y-1)
		self.liberar(x+1, y-1)
		self.liberar(x+1, y)
		self.liberar(x+1, y+1)
		self.liberar(x, y+1)
		self.liberar(x-1, y+1)



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


