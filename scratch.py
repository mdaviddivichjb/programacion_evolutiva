import pyautogui as robot
import time

# Función que pide material
def pido_material():
    mat = robot.prompt(text="Ingrese la cantidad de unidades a solicitar \n " +
                                 "1) Tonner negro \n " +
                                 "2) Tonner Magenta \n " +
                                 "3) Tonner Cyan \n " +
                                 "4) Tonner Amarillo \n " +
                                 "0) FIN", title="Ingrese el material a solicitar", default='')
    if mat == "1":
        material = "CE410X"
    elif mat == "2":
        material = "CE413A"
    elif mat == "3":
        material = "CE411A"
    elif mat == "4":
        material = "CE412A"
    elif mat == "0":
        material = "FIN"

    return material


###################################################################################################
# Ingreso lineas del pedido
###################################################################################################
fin = True
salto = 1

while fin:
    material = pido_material()
    if material == "FIN":
        fin = False
    else:
        print(material)
