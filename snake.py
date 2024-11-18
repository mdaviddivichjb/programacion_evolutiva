"""
 Sencillo ejemplo de serpiente

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame
import random

# --- Globales ---
# Colores}
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255,0,0)

# Establecemos el largo y alto de cada segmento de la serpiente
largodel_segmento = 15
altodel_segmento = 15
# Margen entre cada segmento
margendel_segmento = 3

#Velocidad inicial
cambio_x = largodel_segmento + margendel_segmento
cambio_y = 0

class Segmento(pygame.sprite.Sprite):
    """ Clase que representa un segmento de la serpiente. """
    # -- Métodos
    #  Función constructor
    def __init__(self, x, y):
        # Llamada al constructor padre
        super().__init__()

        # Establecemos el alto y largo
        self.image = pygame.Surface([largodel_segmento, altodel_segmento])
        self.image.fill(BLANCO)

        # Establecemos como punto de partida la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Obstaculo(pygame.sprite.Sprite):
    """ Clase que representa un Obstaculo. """
    # -- Métodos
    #  Función constructor
    def __init__(self, x, y):
        # Llamada al constructor padre
        super().__init__()

        # Establecemos el alto y largo
        self.image = pygame.Surface([largodel_segmento, altodel_segmento])
        self.image.fill(ROJO)

        imagen = pygame.image.load("C:/tmp/borrar/cuerpo.bmp")
        self.image.blit(imagen, (0, 0))

        # Establecemos como punto de partida la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Inicializamos Pygame
pygame.init()

# Inicializo los fuentes
font = pygame.font.SysFont('Comic_sans', 20, True, False)

# Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([800, 600])

# Creamos un título para la ventana
pygame.display.set_caption('Serpiente')

listade_todoslos_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()
# Creamos el primer obstaculo
l_cuadrado = (largodel_segmento + margendel_segmento)
coord_x = random.randint(l_cuadrado, (pantalla.get_width() - l_cuadrado ) )
coord_y = random.randint(l_cuadrado, (pantalla.get_height() - l_cuadrado ) )
obstaculo = Obstaculo(coord_x,coord_y)



# Creamos la serpiente inicial.
segementos_dela_serpiente = []
for i in range(15):
    x = 250 - (largodel_segmento + margendel_segmento) * i
    y = 30
    segmento = Segmento(x, y)
    segementos_dela_serpiente.append(segmento)
    listade_todoslos_sprites.add(segmento)

# Puntuación inicial
puntaje = 0

obstaculos.add(obstaculo)

reloj = pygame.time.Clock()
hecho = False

while not hecho:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

        # Establecemos la velocidad basándonos en la tecla presionada
        # Queremos que la velocidad sea la suficiente para mover un segmento
        # más el margen.
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                cambio_x = (largodel_segmento + margendel_segmento) * -1
                cambio_y = 0
            if evento.key == pygame.K_RIGHT:
                cambio_x = (largodel_segmento + margendel_segmento)
                cambio_y = 0
            if evento.key == pygame.K_UP:
                cambio_x = 0
                cambio_y = (altodel_segmento + margendel_segmento) * -1
            if evento.key == pygame.K_DOWN:
                cambio_x = 0
                cambio_y = (altodel_segmento + margendel_segmento)

    # Eliminamos el último segmento de la serpiente
    # .pop() este comando elimina el último objeto de una lista.
    segmento_viejo = segementos_dela_serpiente.pop()
    listade_todoslos_sprites.remove(segmento_viejo)

    # Determinamos dónde aparecerá el nuevo segmento
    x = segementos_dela_serpiente[0].rect.x + cambio_x
    y = segementos_dela_serpiente[0].rect.y + cambio_y
    segmento = Segmento(x, y)

    # Insertamos un nuevo segmento en la lista
    segementos_dela_serpiente.insert(0, segmento)
    listade_todoslos_sprites.add(segmento)

    # -- Dibujamos todo
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)

    listade_todoslos_sprites.draw(pantalla)
    obstaculos.draw(pantalla)

    # Imprimo puntuación

    mensaje_puntaje = "Puntaje : %d" % puntaje
    text_surface = font.render(mensaje_puntaje, True, [0,255,0])
    pantalla.blit(text_surface, [5, 5])

    # Actualizamos la pantalla
    pygame.display.flip()

    # Verifico si hay colisiones
    lista_colisiones = pygame.sprite.spritecollide(obstaculo, listade_todoslos_sprites, False)
    if ( len(lista_colisiones) > 0):
        puntaje += 20
        coord_x = random.randint(l_cuadrado, (pantalla.get_width() - l_cuadrado ) )
        coord_y = random.randint(l_cuadrado, (pantalla.get_height() - l_cuadrado ) )
        obstaculo.rect.x = coord_x
        obstaculo.rect.y = coord_y


    # Pausa
    reloj.tick(15)

pygame.quit()
