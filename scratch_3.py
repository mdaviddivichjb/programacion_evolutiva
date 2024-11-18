import matplotlib.pyplot as plt

def peano_curve(puntos,order,tipo):

    x = puntos[0][0]
    y = puntos[0][1]
    largo_i = (puntos[1][1] - y)
    largo_o = largo_i /3
    curva = []
    margen = largo_o / 9
    largo = largo_o - (2 * margen)
    if order == 1:
        if tipo == 1:
            curva =  [( (x + margen), (y + margen)),((x+margen) ,(y+margen) + largo_i),((x+margen) + (largo_i/2),(y+margen) + largo_i),((x+margen) + (largo_i/2),(y + margen)),(x+margen+largo_i,y+margen),(x+margen+largo_i, y+margen+largo_i)]
            curva = curva + [ (x,y), (x,y+ largo_i),(x + (largo_i),y + (largo_i)),(x+largo_i,y),(x,y)]
        else:
            # curva = [(x+margen+largo, y+largo + (margen *3)),(x+margen+largo, y+(largo*2) + (margen *3)), (x+margen+(largo/2), y+ (largo*2) + (margen *3)),(x+margen+(largo/2), y+largo + margen *3), (x+margen, y+largo + margen *3),(x+margen, y+largo*2 + (margen *3)) ]
            curva = [(x+margen+largo_i, y + margen),(x+margen+largo_i, y+largo_i+ margen), (x+margen+(largo_i/2), y+ largo_i +margen),(x+margen + (largo_i/2), y + margen), (x+margen, y+margen),(x+margen, y+largo_i + margen) ]
            curva = curva + [ (x,y), (x,y+ (largo_i)),(x + (largo_i),y + (largo_i)),(x+largo_i,y),(x,y)]
    else:
        curva = curva + peano_curve( [(x,y),              (x + largo_o,y + largo_o)], order -1,1)
        curva = curva + peano_curve( [(x,y + largo_o),    (x + largo_o,y + (largo_o*2))], order -1,2)
        curva = curva + peano_curve( [(x,y + (largo_o*2)),(x + largo_o,y + (largo_o*3))], order -1,1)

        #curva = curva + peano_curve( [(x + (largo_o),y + (largo_o*3)),(x + (largo_o*2),y + (largo_o*2))], order -1,2)
        #curva = curva + peano_curve( [(x + (largo_o),y + largo_o*2),(x + (largo_o*2),y +largo_o)], order -1,1)
        #curva = curva + peano_curve( [(x + (largo_o),y+largo_o),(x + (largo_o*2),y )], order -1,2)

        curva = curva + peano_curve( [(x + (largo_o),y ),(x + (largo_o*2),y + (largo_o))], order -1,2)
        curva = curva + peano_curve( [(x + (largo_o),y + largo_o),(x + (largo_o*2),y +largo_o*2)], order -1,1)
        curva = curva + peano_curve( [(x + (largo_o),y+largo_o*2),(x + (largo_o*2),y +largo_o*3)], order -1,2)

        curva = curva + peano_curve( [(x + (largo_o*2),y),(x + (largo_o*3),y + largo_o)], order -1,1)
        curva = curva + peano_curve( [(x + (largo_o*2),y + largo_o),(x + (largo_o*3),y + (largo_o*2)) ], order -1,2)
        curva = curva + peano_curve( [(x + (largo_o*2),y + (largo_o*2)),(x + (largo_o*3),y + (largo_o*3))], order -1,1)

    return(curva)



def plot_peano_curve(order):
    l_points = peano_curve([(0,0),(9,9)],order,1)
    print(l_points)
    plt.figure(figsize=(9, 9))
    x, y = zip(*l_points)
    print(x,y)
    plt.plot(x, y, marker='o', markersize=1)

    plt.title(f'Curva de Peano - Orden {order}')
    plt.axis('equal')
    plt.axis('off')
    plt.show()
# Cambia el orden aquí para obtener diferentes niveles de detalle
plot_peano_curve(order=1)
