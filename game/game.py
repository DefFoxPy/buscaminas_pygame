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

		self.font = pygame.font.match_font(FONT)

		self.dir = os.path.dirname(__file__)
		#self.dir_sounds = os.path.join(self.dir, 'sources/sounds')
		self.dir_images = os.path.join(self.dir, 'sources/image')

	def start(self):
		self.new()

	def new(self):
		self.tablero = Tablero()
		self.game_over = False
		self.puntaje = 0
		self.text_final = '' # mensaje que se mostrará al final de una partida
		self.run()

	def run(self):
		while self.running:
			self.events() 
			self.update() 
			self.draw() 
			self.clock.tick(FPS)

	def events(self):
		for event in pygame.event.get():
		
			if event.type == pygame.QUIT:  
				self.running = False
				pygame.quit()
				sys.exit()

			key = pygame.key.get_pressed()

			if key[pygame.K_r] and self.game_over:
				self.new()
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				if not self.game_over:
					
					x, y = pixeles_a_indice(pygame.mouse.get_pos())
					
					if not coordenada_valida(x, y): continue

					if event.button == CLIC_IZQUIERDO:
						if not self.tablero.get_bandera(x, y):
							self.puntaje += PUNTOS 
							self.tablero.liberar(x, y)
							self.tablero.set_visible(x, y, True)
							
							if self.tablero.hay_mina(x, y):
								self.puntaje -= PUNTOS
								self.text_final = TEXTO_PERDIO
								self.tablero.revelar_todas_las_minas()
								self.stop()

							if self.tablero.todas_casillas_liberadas():
								self.text_final = TEXTO_GANO
								self.stop()

					if event.button == CLIC_DERECHO:
						if not self.tablero.get_visible(x, y):
							self.tablero.cambiar_bandera(x, y)	

	def update(self):
		pass

	def stop(self):
		self.game_over = True

	def draw(self):
		self.surface.fill(WHITE)
		self.tablero.mostrar(self.surface, self.dir_images)
		display_text(self.surface, self.font, "Puntaje actual: " + str(self.puntaje), 20, BLACK, WIDTH//2, 30)

		if self.game_over:
			display_text(self.surface, self.font, self.text_final, 20, BLACK, WIDTH//2, 10)
		pygame.display.update()

