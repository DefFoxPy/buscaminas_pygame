import pygame
import sys
import os

from .config import *
from .tablero import Tablero
from .helper import *


class Game:

	def __init__(self):

		pygame.init()
		self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

		pygame.display.set_caption(TITLE)

		self.running = True

		self.clock = pygame.time.Clock()

		self.dir = os.path.dirname(__file__)
		#self.dir_sounds = os.path.join(self.dir, 'sources/sounds')
		self.dir_images = os.path.join(self.dir, 'sources/image')

	def start(self):
		''' da comienzo al juego '''
		self.new()

	def new(self):
		''' Inicializa una instancia del juego '''
		self.tablero = Tablero()
		self.game_over = False
		self.run()

	def run(self):
		''' ciclo principal del juego '''
		while self.running:
			self.events() 
			self.update() 
			self.draw() 
			self.clock.tick(FPS)

	def events(self):
		''' Manejo de todos los eventos del juego '''
		for event in pygame.event.get():
			# El usuario presionó la tecla de salir
			if event.type == pygame.QUIT:  
				self.running = False
				pygame.quit()
				sys.exit()
			# El usuario precionó una casillas
			if event.type == pygame.MOUSEBUTTONDOWN:
				if not self.game_over:
					# obtenemos el equivalente en x, y de la posicion del mouse
					x, y = pixeles_a_indice(pygame.mouse.get_pos())
					# en caso de que el usuario tecleo fuera del tablero salimos del ciclo
					if not coordenada_valida(x, y): continue

					if event.button == CLIC_IZQUIERDO:
						if not self.tablero.get_bandera(x, y): 
							self.tablero.liberar(x, y) # to do
							self.tablero.set_visible(x, y, True)

					if event.button == CLIC_DERECHO:
						if not self.tablero.get_visible(x, y):
							self.tablero.cambiar_bandera(x, y)	

	def update(self):
		'''Actualiza cada fotograma del juego'''
		pass


	def draw(self):
		'''Dibuja todos los elemenentos en pantalla'''
		self.surface.fill(WHITE)
		self.tablero.mostrar(self.surface, self.dir_images)
		pygame.display.update()
