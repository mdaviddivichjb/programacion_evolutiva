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
#      Función para girar dibujo

def giro(resultado,tipo,p_i,p_f):
    x,y = p_i
    x1,y1 = p_f
    resultado2 = []

    for aux in range(0,len(resultado)):
        a = resultado[aux][0] - (x +((x1-x)/2))
        b = resultado[aux][1] - (y +((y1-y)/2))
        c , d = tipo
        a1 = (a*c - b*d)
        b1 = (a*d + b*c)
        resultado2 = resultado2 + [ ( a1 + (x + ((x1-x)/2)),b1 + (y + ((y1-y)/2)) )]
    print("Resultado: ->", resultado2)
    return resultado2
###########################################################################
#      Función para hacer el Fractal
####################################################################3

def peano(pantalla,p_i,p_f,nivel,tipo,orden):

    # Defino variables
    x,y = p_i
    x1,y1 = p_f

    largo = y1 - y
    margen = largo / 8
    largo_d = largo - (margen * 2)

    lineas = [ ]

    if (nivel == 1):
        # Termino el proceso recursivo

        # Imprimo el patron1

        ##if (orden == 1):
        resultado =  [ (x+margen+ largo_d,y + margen + largo_d), (x+margen+ largo_d,y + margen),(x + margen,y + margen),(x + margen ,
                           y + largo_d + margen )  ]
        ##else:
        ##    resultado =  [ (x + margen,y + largo_d + margen ) ,(x + margen,y + margen), (x+margen+ largo_d,y + margen), (x+margen+ largo_d,y + margen + largo_d)  ]

        return (resultado[0:len(resultado)] )
    else:
        # Comienzo el proceso recursivo

        # cuadrado4
        x,y =  p_i
        x1,y1 = p_f
        x1 = x + largo /2
        y = y + largo /2
        y1 = y + (largo/2)

        peano_aux = peano(pantalla,(x,y),(x1,y1),nivel-1,(0,1),1)
        peano_fin = giro(peano_aux,(0,1),(x,y),(x1,y1))
        if (nivel >= 3 ):
            peano_fin = peano_fin[::-1]

        lineas =  lineas + peano_fin

        # Cuadrado1
        x,y =  p_i
        x1,y1 = p_f
        x1 = x + (largo/2)
        y1 = y + (largo/2)

        peano_aux = peano(pantalla,(x,y),(x1,y1),nivel-1,(1,0),0)

        if (nivel == 2 ):
            peano_aux = peano_aux[::-1]

        lineas =  lineas +  peano_aux

        # Cuadrado2
        x,y =  p_i
        x1,y1 = p_f
        x = x + largo/2
        x1 = x + (largo/2)
        y1 = y + (largo/2)

        peano_aux = peano(pantalla,(x,y),(x1,y1),nivel-1,(1,0),0)

        if (nivel ==  2 ):
            peano_aux = peano_aux[::-1]

        lineas =  lineas +  peano_aux

        # Cuadrado3
        x,y =  p_i
        x1,y1 = p_f
        x1 = x + largo
        y1 = y + largo
        y = y + (largo/2)
        x = x + (largo/2)

        peano_aux = peano(pantalla,(x,y),(x1,y1),nivel-1,(0,-1),1)
        peano_fin = giro(peano_aux,(0,-1),(x,y),(x1,y1))
        if (nivel >= 3):
            peano_fin = peano_fin[::-1]
        lineas =  lineas + peano_fin

        ##lineas = lineas + peano(pantalla,(x,y),(x1,y1),nivel-1,(0,-1),1)



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
lineas =  peano(pantalla,(30,30),(570,570),6,(0,-1),1)
print(lineas)
pygame.draw.lines(pantalla,ROJO,False,lineas)
while not hecho:

    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True



