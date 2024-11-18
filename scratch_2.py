import matplotlib.pyplot as plt

def peano_curve(puntos,order):

    x = puntos[0][0]
    y = puntos[0][1]
    largo = (puntos[1][1] - y) /3
    curva = []
    if order == 1:

        curva = [ [(x, y),(x + largo,y),(x + largo,y + largo),(x,y + largo),(x,y)] ]
        curva.append([(x + largo,y + largo),(x + largo,y + (largo*2)), (x , y + (largo*2)),(x,y + largo)])
        curva.append([ (x + largo,y + (largo*2)), (x + largo,y + (largo*3)), (x,y + (largo*3)),(x,y + (largo*2)) ])
        curva.append([(x + largo,y ), (x + (largo*2),y ), (x + (largo*2),y + largo),(x+largo,y+largo)]  )
        curva.append([(x + (largo*2),y + largo ), (x + (largo*2),y + (largo * 2)), (x + largo,y + (largo*2))]  )
        curva.append([(x + (largo*2),y + (largo *2) ), (x + (largo*2),y + (largo * 3)), (x + largo,y + (largo*3))] )

        curva.append([(x + (largo*2),y ), (x + (largo*3),y ), (x + (largo*3),y + largo),(x+(largo*2),y+largo)]  )
        curva.append([(x + (largo*3),y + largo ), (x + (largo*3),y + (largo * 2)), (x + (largo*2),y + (largo*2))]  )
        curva.append([(x + (largo*3),y + (largo *2) ), (x + (largo*3),y + (largo * 3)), (x + (largo*2),y + (largo*3))] )
    else:
        curva = curva + peano_curve( [(x, y),(x + largo,y + largo)], order -1)
        curva = curva + peano_curve( [(x,y + largo),(x + largo,y + (largo*2))], order -1)
        curva = curva + peano_curve( [(x,y + (largo*2)),(x + largo,y + (largo*3))], order -1)

        curva = curva + peano_curve( [(x + largo,y),(x + (largo*2),y + largo)], order -1)
        curva = curva + peano_curve( [(x + largo,y + largo),(x + (largo*2),y + (largo*2))], order -1)
        curva = curva + peano_curve( [(x + largo,y + (largo*2)),(x + (largo*2),y + (largo*3))], order -1)

        curva = curva + peano_curve( [(x + (largo*2),y),(x + (largo*3),y + largo)], order -1)
        curva = curva + peano_curve( [(x + (largo*2),y + largo),(x + (largo*3),y + (largo*2)) ], order -1)
        curva = curva + peano_curve( [(x + (largo*2),y + (largo*2)),(x + (largo*3),y + (largo*3))], order -1)

    return(curva)



def plot_peano_curve(order):
    l_points = peano_curve([(0,0),(9,9)],order)
    print(l_points)
    plt.figure(figsize=(9, 9))
    for points in l_points:
        x, y = zip(*points)
        print(x,y)
        plt.plot(x, y, marker='o', markersize=1)

    plt.title(f'Curva de Peano - Orden {order}')
    plt.axis('equal')
    plt.axis('off')
    plt.show()
# Cambia el orden aquí para obtener diferentes niveles de detalle
plot_peano_curve(order=4)
