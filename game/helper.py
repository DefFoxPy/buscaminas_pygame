import pygame

def cargar_imagen(direccion, transparente = True):
	try: image = pygame.image.load(direccion)
	except pygame.error as message: raise SystemExit(message)

	image = image.convert()

	if transparente:
		color = image.get_at((0, 0))
		image.set_colorkey(color, pygame.RLEACCEL)

	return image