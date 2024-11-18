"""
 Sencillo ejemplo de Fractal de Peano

 """

import pygame
import random

# --- Globales ---
# Colores}
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255,0,0)

###########################################################################
#      Función para hacer el Fractal
####################################################################3

def peano(pantalla,p_i,p_f,nivel,tipo):

    # Defino variables
    x,y = p_i
    x1,y1 = p_f

    largo = y1 - y
    margen = largo / 8
    largo_d = largo - (margen * 2)

    lineas = [ ]

    if (nivel == 1):
        # Termino el proceso recursivo
        if (tipo == 1):
            # Imprimo el patron1
            resultado =  [(x + margen , y + largo  ),(x + margen,y + margen),(x+margen+ largo_d/2,y + margen),
                                             (x+margen+ largo_d/2,y + margen + largo_d),(x+margen+ largo_d,y + margen+ largo_d),
                                              (x+margen+ largo_d,y )]
            print(resultado)
            return (resultado[0:len(resultado)] )
        else:
            # Imprimo el patron2
            resultado = [(x+margen+ largo_d,y + largo), (x+margen+ largo_d,y + margen), (x+margen+ largo_d/2,y + margen ),
                         (x+margen+ largo_d/2,y + margen + largo_d), (x + margen,y + margen + largo_d),(x + margen , y  ) ]
            print(resultado)
            return (resultado[0:len(resultado)])
    else:
        # Comienzo el proceso recursivo
        x,y =  p_i
        x1,y1 = p_f
        x1 = x + (largo/3)
        y1 = y + (largo/3)


        lineas = lineas + peano(pantalla,(x,y),(x1,y1),nivel-1,1)

        x,y =  p_i
        x1,y1 = p_f
        y1 = y + (largo/3) * 2
        y = y + (largo/3)
        x1 = x + (largo/3)



        lineas =  peano(pantalla,(x,y),(x1,y1),nivel-1,2) + lineas

        x,y =  p_i
        x1,y1 = p_f
        y1 = y + (largo/3) * 3
        y = y + (largo/3) *2
        x1 = x + (largo/3)



        lineas =  peano(pantalla,(x,y),(x1,y1),nivel-1,1) + lineas


        x,y =  p_i
        x1,y1 = p_f
        y1 = y + (largo/3) * 2
        y = y + (largo/3) *3
        x1 = x + (largo/3)
        x = x + (largo/3) * 2
        lineas =  peano(pantalla,(x,y),(x1,y1),nivel-1,2) + lineas

        x,y =  p_i
        x1,y1 = p_f
        y1 = y + (largo/3)
        y = y + (largo/3) *2
        x1 = x + (largo/3)
        x = x + (largo/3) * 2
        lineas =  peano(pantalla,(x,y),(x1,y1),nivel-1,1) + lineas

        x,y =  p_i
        x1,y1 = p_f
        y1 = y
        y = y + (largo/3)
        x1 = x + (largo/3)
        x = x + (largo/3) * 2
        lineas =  peano(pantalla,(x,y),(x1,y1),nivel-1,2) + lineas

        x,y =  p_i
        x1,y1 = p_f
        x1 = x + (largo/3)*3
        x= x + (largo/3)*2
        y1 = y + (largo/3)

        lineas = peano(pantalla,(x,y),(x1,y1),nivel-1,1) + lineas

        x,y =  p_i
        x1,y1 = p_f
        x1 = x + (largo/3)*3
        x= x + (largo/3)*2
        y1 = y + (largo/3) *2
        y = y + (largo/3)

        lineas = peano(pantalla,(x,y),(x1,y1),nivel-1,2) + lineas

        x,y =  p_i
        x1,y1 = p_f
        x1 = x + (largo/3)*3
        x= x + (largo/3)*2
        y1 = y + (largo/3) *3
        y = y + (largo/3) *2

        lineas = peano(pantalla,(x,y),(x1,y1),nivel-1,2) + lineas

    return (lineas[0:len(lineas)])


###################################################################################################
#                                                    Programa Principal
###################################################################################################

# Inicializamos Pygame
pygame.init()

# Inicializo los fuentes
font = pygame.font.SysFont('Comic_sans', 20, True, False)

# Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([600, 600])

# Creamos un título para la ventana
pygame.display.set_caption('Fractal de Peano')


hecho = False

lineas = []

# Dibujo el fractal
lineas =  peano(pantalla,(30,30),(570,570),2,1)
print(lineas)
pygame.draw.lines(pantalla,ROJO,False,lineas)
while not hecho:

    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True



