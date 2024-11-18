import pyautogui as robot
import time

sap = 520,219
prd_produc = 960,296

# Función para movilizar el mouse y dar un click
def abrir(pos,click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

# Función para escribir
def escribo(mensaje,tiempo):
    robot.typewrite(mensaje,tiempo)

# Función para Seleccionar ambiente PRD
def selec_ambiente():
    lugar = robot.locateCenterOnScreen("C:\\tmp\\sap_produc1.png")
    lugar = ((lugar.x + 350 , lugar.y + 50) )
    abrir(lugar,click=2)

    time.sleep(2)

#Función para Ingresar usuario mdavidovich
def ing_usuario():
    escribo("mdavidovich",0.05)
    robot.hotkey('tab')
    passw = robot.password(text='Ingrese la contraseña', mask='*')
    escribo(passw,0.03)
    robot.hotkey('enter')

    time.sleep(2)

# Función para seleccionar la opción de pedir material
def sel_pedir_mat():
    lugar2 = robot.locateOnScreen("C:\\tmp\\sap_pedir_mat.png")

    lugar3 = lugar2[0] + 90,lugar2[1] + 150
    abrir(lugar3,click=2)

    time.sleep(2)

# Función para pedir por pantalla la cantidad a pedir
def pido_cant():

    cantidad_p = robot.password(text='Ingrese la cantidad de unidades a solicitar', mask='*')

    time.sleep(2)
    return cantidad_p


# Función que ingresa la cantidad a pedir
def ing_cant(cantidad_p):

    # Ingreso la cantidad a pedir
    lugar2 = robot.locateOnScreen("C:\\tmp\\ingreso_cantidad.png")

    lugar3 = lugar2[0] + 40,lugar2[1] + 40
    abrir(lugar3,click=1)

    escribo(cantidad_p,0.03)
    robot.hotkey('enter')

    time.sleep(2)

# Función que pide material
def pido_material():
    mat = robot.prompt(text="Ingrese el material a solicitar \n " +
                                 "1) Tonner Negro \n " +
                                 "2) Tonner Cyan  \n " +
                                 "3) Tonner Amarillo \n " +
                                 "4) Tonner Magenta \n " +
                                 "0) FIN", title="Ingrese el material a solicitar", default='')
    if mat == "1":
        material = "100000481"
    elif mat == "2":
        material = "100000482"
    elif mat == "3":
        material = "100000483"
    elif mat == "4":
        material = "100000484"
    elif mat == "0":
        material = "FIN"

    return material


#Función para ingresar la necesidad

def ing_necesidad():
    lugar2 = robot.locateOnScreen("C:\\tmp\\ingreso_necesidad.png")

    lugar3 = lugar2[0] + 40,lugar2[1] + 40
    abrir(lugar3,click=1)

    escribo("AI601",0.03)
    robot.hotkey('enter')

    time.sleep(2)


def ingreso_linea(traslado):

    ###################################################################################################
    # Ingreso linea con tonner
    ###################################################################################################
    time.sleep(2)
    # Selecciono la opción de material a pedir
    lugar2 = robot.locateOnScreen("C:\\tmp\\material.png")

    lugar3 = lugar2[0] + (20 * traslado),lugar2[1] + (30 * traslado)
    abrir(lugar3,click=2)

    time.sleep(2)

    # Pido el código del material a solicitar

    mat_pedido = pido_material()

    retorno = 1

    if mat_pedido == "FIN":
        retorno = 0
    else:
        escribo(mat_pedido,0.03)
        robot.hotkey('enter')

        time.sleep(2)

        # Pido por pantalla la cantidad a pedir

        cantidad_p = pido_cant()

        # Ingreso la cantidad a pedir
        ing_cant(cantidad_p)

        # Ingreso la necesidad
        ing_necesidad()

    return retorno
################################################################################
# Programa principal
################################################################################

# Minimizo ventanas
robot.hotkey('winleft','d')

#Abrir SAP
abrir(sap,click=2)

time.sleep(5)

#Seleccionar ambiente PRD
selec_ambiente()

#Ingresar usuario mdavidovich
ing_usuario()

# Selecciono la opción de pedir material
sel_pedir_mat()

###################################################################################################
# Ingreso lineas del pedido
###################################################################################################
fin = True
salto = 1

while fin:
    result = ingreso_linea(salto)
    salto = 2

    if result == 0:
        fin = False


