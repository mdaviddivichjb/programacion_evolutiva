from random import *
##import numpy as np
import csv

# Programa genetico para jugar al ta te ti
print('juguemos al ta te ti!')

# La estructura de los Genes serìa la siguiente
#  * Est_i (1..1000) * Entrada (1..9) * Salida (1..9) * Est_f (1..1000)*


# Función que devuelve el tablero, agregando la jugada
def marco_jugada(tablero,jugada_cruz,jugador,l_vacios):

    fila = (jugada_cruz-1) // 3
    columna = jugada_cruz % 3
    tablero [fila ][columna-1 ]= jugador

    l_vacios = [x for x in l_vacios if x != jugada_cruz]
    return [tablero,l_vacios]

# Función que devuelve si hay lugares vacíos en el tablero
def hay_vacios (tablero):
    resultado = False
    for linea in tablero:
        #print(linea)
        if (linea[0] == 0 or linea[1] == 0 or linea[2] == 0 ):
            resultado = True
    return resultado

# Función que devuelve la tupla para un estado y una entrada
def busco_tupla (est,ent,tabla_estados):
    for tupla_aux in tabla_estados:
        if (tupla_aux[0] == est  and tupla_aux[1] == ent):
            return tupla_aux
    return([])

def genero_tabla_est (tabla_est, cant_ent):
    for aux1 in range(1,(cant_ent +1)):
        for aux2 in range(1,10):
            list_est_s = [x for x in range(1,(cant_ent +1)) if x != aux1]
            list_val_s = [x for x in range(1,7) if x != aux2]

            # Genero estado salida
            est_s = randint(1,cant_ent)

            # Genero valor de salida
            val_s = randint(1,6)

            # Agrego valor al tablero
            tabla_est = tabla_est + [[aux1,aux2,val_s,est_s]]


    return tabla_est

# Función que devuelve el resultado del algoritmo en función de la jugada oponente

def resultado_algoritmo(jugada_cruz,estado,tabla_estados,l_vacios):

    jugada_aux = busco_tupla(estado,jugada_cruz,tabla_estados)
    jugada_cero = jugada_aux[2]
    estado_f = jugada_aux[3]
    res_aux = [x for x in l_vacios if x == jugada_cero]
    if (len(res_aux) < 1):
        jugada = randint(0,(len(l_vacios)-1))
        jugada_cero = l_vacios[jugada]

    return [jugada_cero,estado_f]

def busco_ganador(tablero):
    if ((tablero[0][0] == tablero[0][1] ) and (tablero[0][1] == tablero[0][2] ) and tablero[0][0] >0):
        return True

    if ((tablero[1][0] == tablero[1][1] ) and (tablero[1][1] == tablero[1][2] ) and tablero[1][0] >0):
        return True

    if ((tablero[2][0] == tablero[2][1] ) and (tablero[2][1] == tablero[2][2] ) and tablero[2][0] >0):
        return True

    if ((tablero[0][0] == tablero[1][0] ) and (tablero[1][0] == tablero[2][0] ) and tablero[0][0] >0):
        return True

    if ((tablero[0][1] == tablero[1][1] ) and (tablero[1][1] == tablero[2][1] ) and tablero[0][1] >0):
        return True

    if ((tablero[0][2] == tablero[1][2] ) and (tablero[1][2] == tablero[2][2] ) and tablero[0][2] >0):
        return True

    if ((tablero[0][0] == tablero[1][1] ) and (tablero[1][1] == tablero[2][2] ) and tablero[0][0] >0):
        return True

    if ((tablero[0][2] == tablero[1][1] ) and (tablero[1][1]== tablero[2][0] ) and tablero[0][2] >0):
        return True

    return False

####################################################
# Función que simula un juego
def simulo_juego (tabla_estados):
    # Simulo juego
    tablero = [ [0,0,0],[0,0,0],[0,0,0] ]
    l_vacios = [1,2,3,4,5,6,7,8,9]
    estado = 1
    hay_ganador = False

    while hay_vacios(tablero) and (not(hay_ganador)):

        jugada = randint(0,(len(l_vacios)-1))
        jugada_cruz = l_vacios[jugada]

        res = marco_jugada(tablero,jugada_cruz,1,l_vacios)
        tablero = res[0]
        hay_ganador = busco_ganador(tablero)
        if hay_ganador:
            return 1

        l_vacios = res[1]

        if (len(l_vacios) >0 and (not(hay_ganador))):
            jugada_res = resultado_algoritmo(jugada_cruz,estado,tabla_estados,l_vacios)

            jugada_cero = jugada_res[0]
            estado = jugada_res[1]
            res = marco_jugada(tablero,jugada_cero,2,l_vacios)
            tablero = res[0]
            l_vacios = res[1]

            hay_ganador = busco_ganador(tablero)
            if hay_ganador:
                return 2
    return 0



# Función que genera puntaje de un individuo
###################################################################################

def genero_puntaje_ind(individuo,c_pruebas):
    resultado = [0,0,0]
    ponderacion = [4,-6,5]
    for aux in range(1,c_pruebas):
        res = simulo_juego(individuo)
        resultado[res] = resultado[res] +1

    # puntuo diferente cada tipo de resultado
    res = (resultado[0] * ponderacion[0]) + (resultado[1] * ponderacion[1]) + (resultado[2] * ponderacion[2])
    return res

def genero_puntaje_ind_1(individuo):

    return genero_puntaje_ind(individuo,25)

# Función para generar Poblacion
###################################################################################

def genero_poblacion(c_indiv):
    individuos = []
    for aux in range(0,c_indiv):
        individuos_aux = genero_tabla_est([],c_estados)
        individuos = individuos + [individuos_aux]

    return individuos

# Función para calificar a los individuos de una Poblacion
###################################################################################
def califico_poblacion(poblacion,c_pruebas):
    resultados = []
    for aux in range(0,len(poblacion)):
        resultados_aux = genero_puntaje_ind(poblacion[aux],c_pruebas)
        resultados = resultados + [resultados_aux]

    return resultados


def cruzo_individuos(ind1,ind2):
    p_cruce1 = len(ind1)/3
    p_cruce2 = p_cruce1 * 2

    hijo = []

    # comienzo proceso de cruce
    for aux in range(0,len(ind1)):
        if (aux <= p_cruce1):
            hijo = hijo + [ind1[aux]]
        elif (aux > p_cruce1 and aux <= p_cruce2):
            hijo = hijo + [ind2[aux]]
        else:
            hijo = hijo + [ind1[aux]]

    return hijo

# Función para elegir los individuos que se van a reproducir
def elijo_rep(poblacion,calificacion_pob,c_reproducciones):

    # La elección va a ser en base a ruleta

    # Genero la ruleta
    ruleta = []
    for aux in range(0,len(calificacion_pob)):
        if (calificacion_pob[aux] > 0 ):
            for aux2 in range (0,(calificacion_pob[aux]*100)):
                ruleta = ruleta + [aux]
    if (len(ruleta) == 0):
        print ("Ruleta:",ruleta)
        ruleta = [1,1]
    # Genero lista de reproductores
    reproductores = []
    for aux in range(0,c_reproducciones):
        numero_azar = randint(0,(len(ruleta)-1) )
        #print("ruleta:",ruleta, "nro_azar",numero_azar)
        reproductor = ruleta[numero_azar]
        reproductores = reproductores + [reproductor]

    return reproductores

# Función que hace las reproducciones
def hago_reproducciones(poblacion,lista_rep):

    lista_hijos = []
    # Hago las reproducciones
    # Saco de la población los individuos más desfavorecidos
    poblacion_filt = [x for x in poblacion if genero_puntaje_ind(x,c_pruebas) > 0]
    if (len(poblacion_filt) == 0):
        poblacion_filt = poblacion
    for aux in range(0,len(lista_rep)):
        # Hago reproducción
        indice_pareja = randint(0,(len(poblacion_filt)-1))
        pareja = poblacion_filt[indice_pareja]
        hijo = cruzo_individuos(lista_rep[aux],pareja)
        lista_hijos = lista_hijos + [hijo]

    return lista_hijos

def devuelvo_puntaje(x):

    return x[0]

# Programa que agrega hijos a la poblacion
def agrego_hijos_pob(poblacion,hijos):

    tam_pob = len(poblacion)
    for aux in range(0,len(hijos)):
        # Agrego al hijo en la poblacion
        poblacion = poblacion + [hijos[aux]]

    print("Poblacion sin ordenar : \n")
    calif_pob_ext = califico_poblacion(poblacion,25)

    # Genero lista aux
    lista_aux = []
    for aux in range(0,len(poblacion)):
        lista_aux = lista_aux + [[calif_pob_ext[aux],aux]]
    print("lista_aux: \n")
    print(lista_aux)

    #Ordeno la población según su puntaje
    lista_aux_ord = sorted(lista_aux,key=devuelvo_puntaje,reverse=True)
    print("lista_aux_ord : \n")
    print(lista_aux_ord)

    pob_resultado = []
    lista_cal = []
    for aux in range(0,tam_pob):
        pob_resultado = pob_resultado + [poblacion[lista_aux_ord[aux][1]]]
        lista_cal = lista_cal + [lista_aux_ord[aux][0]]

    print("Calificacion de la Poblacion Resultado : \n")
    print(lista_cal)

    return pob_resultado

# Programa que recibe una poblacion y una puntuación, y devuelve la que está mejor ranqueada
def busco_mejor_resultado(poblacion,calif_pob):
# Genero lista aux
    lista_aux = []
    for aux in range(0,len(poblacion)):
        lista_aux = lista_aux + [[calif_pob[aux],aux]]

    #Ordeno la población según su puntaje
    calif_pob_ext = sorted(lista_aux,key=devuelvo_puntaje,reverse=True)

    return(calif_pob_ext[0])

# Función que guarda en un archivo la tabla de estados
###################################################################################
def guardar_datos(nombre_arch,datos):
    with open(nombre_arch, "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(datos)

# Función que carga la tabla de estados desde un archivo
###################################################################################
def cargar_datos(nombre_arch):
     with open(nombre_arch, "r", newline='') as f:
        reader = csv.reader(f, delimiter=',')
        datos = [[int(d1), int(d2), int(d3), int(d4)] for d1, d2, d3 , d4 in reader]

     return datos

# Función que juega al Ta Te Ti usando la tabla que recibe como parámetro
###################################################################################
def juego_ta_te_ti(tabla_mejor,tablero):
   partido_sigue = True
   l_vacios = [1,2,3,4,5,6,7,8,9]
   estado = 1
   hay_ganador = False
   while (partido_sigue and not(hay_ganador)):
       #Despliego el Ta Te Ti por pantalla
       print(tablero[0], "\n",tablero[1], "\n",tablero[2], "\n")

       # Pido jugada por pantalla
       jugada_cruz = int(input("Ingrese su jugada :"))

       # Agrego jugada al tablero
       resultado = marco_jugada(tablero,jugada_cruz,1,l_vacios)
       print(resultado)
       tablero_res = resultado[0]
       l_vacios = resultado[1]

       #Despliego el Ta Te Ti por pantalla
       print(tablero_res[0], "\n",tablero_res[1], "\n",tablero_res[2], "\n")

       partido_sigue = hay_vacios(tablero_res)
       hay_ganador = busco_ganador(tablero)

       if (partido_sigue and not(hay_ganador)):
           res = resultado_algoritmo(jugada_cruz,estado,tabla_mejor,l_vacios)
           jugada_maq = res[0]
           estado = res[1]
           resultado = marco_jugada(tablero,jugada_maq,2,l_vacios)
           tablero_res1 = resultado[0]
           l_vacios = resultado[1]

       partido_sigue = hay_vacios (tablero)
       hay_ganador = busco_ganador(tablero)
   #Despliego el Ta Te Ti final por pantalla
   print( tablero_res1[0], "\n",tablero_res1[1], "\n",tablero_res1[2], "\n" )


# Comienza programa principal
###################################################################################
c_indiv = 540
c_estados = 40
c_pruebas = 25
c_reproducciones = 50
c_ciclos_rep = 40

individuos = []
resultados = []

# Genero la poblacion de individuos
poblacion = genero_poblacion(c_indiv)

# Califico a los individuos de la poblacion
calificacion_pob = califico_poblacion(poblacion,c_pruebas)

print("Calificacion Poblacion : \n")
print(calificacion_pob)

# Hago los ciclos de reproducción
for aux in range(0,c_ciclos_rep):

    print("Ciclo nro. :", aux ,"\n")
    # Elijo los individuos que se procrearan
    reproductores = elijo_rep(poblacion,calificacion_pob,c_reproducciones)

    # Genero lista de reproductores
    lista_rep = []
    for aux in range(0,len(reproductores)):
        lista_rep = lista_rep + [poblacion[reproductores[aux]]]

    # Realizo las reproducciones
    hijos = hago_reproducciones(poblacion,lista_rep)
    calificacion_h = califico_poblacion(hijos,c_pruebas)

    # Inserto hijos en la poblacion
    poblacion = agrego_hijos_pob(poblacion,hijos)
    calificacion_pob = califico_poblacion(poblacion,c_pruebas)

# Busco la tabla que tiene mejor puntaje
lugar_tabla_mejor = busco_mejor_resultado(poblacion,calificacion_pob)
tabla_mejor = poblacion[lugar_tabla_mejor[1]]
# Guardo la mejor tabla en un archivo
guardar_datos("C:/tmp/tabla_tateti.csv",tabla_mejor)

fin = False
while not(fin):
    # juego al Ta Te Ti utilizando la mejor tabla
    tablero = [ [0,0,0],[0,0,0],[0,0,0] ]
    resultado = juego_ta_te_ti(tabla_mejor,tablero)

    # Pido si quiere volver a jugar (1 Si, resto no)
    sigue_jugando = int(input("Quiere volver a jugar (0 = Si :"))
    if (sigue_jugando > 0):
        fin = True
