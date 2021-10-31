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
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Alumnos: Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico
    fig, ax = plt.subplots(2,2)
    fig.suptitle('grafica de 2x2')
    ax[0,0].plot(y1, color='g', marker='o', markeredgecolor='k')
    ax[0,0].set_title('x al cuadrado')
    ax[0,1].plot(y2, color='b', marker='v', markeredgecolor='r')
    ax[0,1].set_title('x al cubo')
    ax[1,0].plot(y3, color='y', marker='<', markeredgecolor='m')
    ax[1,0].set_title('x a la cuarta')
    ax[1,1].plot(y4, color='r', marker='*', markeredgecolor='g')
    ax[1,1].set_title('raiz cuadrada (x)')
    plt.grid()
    plt.show()

    print("terminamos")
