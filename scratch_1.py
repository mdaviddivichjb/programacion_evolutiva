import matplotlib.pyplot as plt

def peano_curve(order, x=0, y=0, size=1):
    if order == 0:
        return [(x, y)]

    points = []
    # Tamaño del paso en la siguiente iteración
    new_size = size / 3

    # Generar la curva de Peano
    points += peano_curve(order - 1, x, y, new_size)
    points += peano_curve(order - 1, x + new_size, y, new_size)
    points += peano_curve(order - 1, x + new_size * 2, y, new_size)
    points += peano_curve(order - 1, x + new_size * 2, y + new_size, new_size)
    points += peano_curve(order - 1, x + new_size * 2, y + new_size * 2, new_size)
    points += peano_curve(order - 1, x + new_size, y + new_size * 2, new_size)
    points += peano_curve(order - 1, x, y + new_size * 2, new_size)
    points += peano_curve(order - 1, x, y + new_size, new_size)

    return points

def plot_peano_curve(order):
    points = peano_curve(order)
    x, y = zip(*points)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, marker='o', markersize=1)
    plt.title(f'Curva de Peano - Orden {order}')
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Cambia el orden aquí para obtener diferentes niveles de detalle
plot_peano_curve(order=3)
