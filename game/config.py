# Número de filas y columnas
COLUMNA = 10
FILA = 8

NUMERO_MINAS = 10

# Atributos de las casillas
CASILLA_LARGO = 40
CASILLA_ALTO = 40
CASILLA_LIBRE = 0
CASILLA_MINA = 9
CASILLA_BANDERA = 10

# margen entre las celdas vertical
MARGEN_Y = 55

WIDTH = COLUMNA * CASILLA_LARGO
HEIGHT = FILA * CASILLA_ALTO + MARGEN_Y

# Mouse
CLIC_IZQUIERDO = 1
CLIC_DERECHO = 3

FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR_EXPLORADO_1 = (229, 194, 159)
COLOR_EXPLORADO_2 = (215, 184, 153)
COLOR_OCULTO_1 = (170, 215, 81)
COLOR_OCULTO_2 = (162, 209, 73)

# Titulo del juego
TITLE = 'Buscaminas'

FONT = 'Arial'

TEXTO_GANO   = 'Felicidades, presiona "r" para volver a jugar' 
TEXTO_PERDIO = 'Perdiste, presiona "r" para volvera jugar'

IMAGENES = [None, 'numero_1.png', 'numero_2.png', 'numero_3.png', 'numero_4.png', \
		    'numero_5.png', 'numero_6.png', 'numero_7.png', 'numero_8.png', 'mina.png', \
		    'bandera.png']