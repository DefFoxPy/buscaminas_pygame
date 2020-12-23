import pygame
import sys
import os


from .config import *
from .tablero import Tablero

class Game:

	def __init__(self):

		pygame.init()
		self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

		pygame.display.set_caption(TITLE)

		self.tablero = Tablero()

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

	def update(self):
		'''Actualiza cada fotograma del juego'''
		pass

	def draw(self):
		'''Dibuja todos los elemenentos en pantalla'''
		self.surface.fill(WHITE)
		self.tablero.mostrar(self.surface)
		pygame.display.update()
