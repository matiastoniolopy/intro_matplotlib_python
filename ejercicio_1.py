# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Alumnos: Se desea graficar los valores de "x" e "y" en un gráfico de línea

    # Función que se desea graficar:
    # y = x**2

    x = list(range(-10, 11, 1))

    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    # Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "y" en función de "x"

    # Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    # Crear acá su gráfico
    fig = plt.figure()
    fig.suptitle('line plot')
    ax = fig.add_subplot()
    ax.plot(y, x, color='g', marker='*',markersize=12, markerfacecolor='y', markeredgecolor='r', linestyle='--', label='y = x**2')
    plt.xlabel('eje x')
    plt.ylabel('eje y')
    plt.axhspan(0.0,10.0, color='pink', alpha=0.2)
    ax.set_facecolor('orange')
    ax.grid()
    ax.legend()
    plt.show()




    print("terminamos") 