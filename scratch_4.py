"""
 Sencillo ejemplo de Fractal de Peano

 """

from PIL import Image, ImageDraw
import numpy as np

import random

# --- Globales ---
# Colores
size = 50,50

imagen1 = Image.open("C:/tmp/dib_1.bmp")
imagen2 = Image.open("C:/tmp/dib_vacio.bmp")

imagen2_dib = ImageDraw.Draw(imagen2)

imagen2_dib.ellipse((100,100,120,120), fill = 'black', outline = 'black')
imagen2_dib.ellipse((140,140,160,160), fill = 'black', outline = 'black')
imagen2_dib.ellipse((180,180,200,200), fill = 'black', outline = 'black')


im_array1 = np.asarray(imagen1)
im_array2 = np.asarray(imagen2)
im_array3 = np.array(imagen2_dib)

im_array1 = im_array1.astype('u1')
im_array2 = im_array2.astype('u1')


#imagen3 = Image.fromarray(im_array3)
# imagen3.save("C:/tmp/byn3.bmp")
imagen2.save("C:/tmp/byn3.bmp")

print(np.array(imagen2))
#---------------------------------------------------------------------
# Comienza Programa Principal

# Inicializamos Pygame

#
