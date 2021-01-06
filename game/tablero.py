from .config import *
from .casilla import Casilla
from .helper import *

class Tablero:

	def __init__(self):
		self.t = list() # tablero representado como una lista de listas
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

	def agregar_minas(self):
		""" Posiciona de forma aleatoria el NUMERO_MINAS del juego dentro del tablero """
		from random import randint

		minas_agregadas = 0

		while minas_agregadas < NUMERO_MINAS:
			# crea una coordenada aleatoria (x, y)
			x = randint(0, COLUMNA-1)
			y = randint(0, FILA-1)

			if self.t[x][y].get_contenido() != CASILLA_MINA:
				self.t[x][y].set_contenido(CASILLA_MINA)
				minas_agregadas += 1

	def agregar_numeros(self):
		""" determina cual será el contenido de cada casilla según las minas se sus casillas vecinas """
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

	def mostrar(self, surface, dir_images):
		""" Dibuja el tablero en pantalla """
		for x in range(COLUMNA):
			for y in range(FILA):
				self.t[x][y].mostrar(surface, dir_images)

	def liberar(self, x, y):
		""" Algoritmo recursivo encargado de establecer como visible una casilla (x,y)
		
		*** Caso base ***
		Por cada casilla se hacen las siguientes preguntas
		1) ¿las coordenadas de la casilla son valídas?
		2) ¿La casilla es visible?
		3) ¿hay una mina en la casilla?

		si la repuesta es no para las anteriores preguntas

		4) ¿el contenido de la casilla es un número? 
		   entonces establecer la casilla como visible

		5) ¿la casilla no contiene nada (casilla libre)?
		   entonces establecer la casilla como visible 


		*** Caso recursivo ***
		recorrer las 8 casillas que hay alrededor de la casilla actual

		Parámetros:
			x(int): posicion x de la casilla
			y(int): posicion y de la casilla

		"""
		# Casos bases
		if not coordenada_valida(x, y): return # 1
		if self.t[x][y].get_visible(): return # 2
		if self.t[x][y].get_contenido() == CASILLA_MINA: return # 3

		if self.t[x][y].get_contenido() not in [CASILLA_LIBRE, CASILLA_MINA]: # 4
			self.t[x][y].set_visible(True)
			return 

		if self.t[x][y].get_contenido() == CASILLA_LIBRE: # 5
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

	def hay_mina(self, x, y):
		""" determina si en una casilla recien descubierta habia una mina 
		
		Parámetros:
			x(int): posicion en x
			y(int): posicion en y

		Returns:
			True si hay una mina, caso contrario False
		"""
		return self.t[x][y].get_contenido() == CASILLA_MINA

	def todas_casillas_liberadas(self):
		""" determina si ya el usuario ha despejado todas las casillas sin minas """
		despejado = True # asume que las casilla están despejadas
		for x in range(COLUMNA):
			for y in range(FILA):
				# obtenemos los datos de la casilla
				visible = self.t[x][y].get_visible()
				contenido = self.t[x][y].get_contenido()

				if not visible and contenido != CASILLA_MINA:
					despejado = False # aún faltan minas

		return despejado

	def get_bandera(self, x, y):
		""" obtiene el estado del atributo bandera de una casilla en particular """
		return self.t[x][y].get_bandera()

	def get_contenido(self, x, y):
		""" Obtiene el contenido de la casilla correspondiente """
		return self.t[x][y].get_contenido()

	def get_visible(self, x, y):
		""" obtiene el estado del atributo 'visible' de una casilla en particular """
		return self.t[x][y].get_visible()

	def set_visible(self, x, y, estado):
		""" cambia el estado de visibilidad de una casilla en particular """
		self.t[x][y].set_visible(estado)

	def cambiar_bandera(self, x, y):
		""" si hay bandera en una casilla la quita y viceversa """
		self.t[x][y].set_bandera(not self.t[x][y].get_bandera())


