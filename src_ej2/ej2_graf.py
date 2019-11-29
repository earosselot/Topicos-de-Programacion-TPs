import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import scipy
import numpy as np


def Sort(sub_li, elem):
    # ordena la lista de listas segun un elemento pasado como parametro (elem)

    return (sorted(sub_li, key=lambda x: x[elem]))

def get_item(list, item):
    """devuelve una lista con el enesimo elemento de cada lista de una lista (de listas)"""

    res = []
    for elem in list:
        res.append(float(elem[item]))
    return res


with open('resultados_final.csv', 'r') as resultados:

    # leo los datos del .csv y los guardo en matriz_res
    matriz_res = []
    for linea in resultados:
        linea = linea.strip('\n')
        camposDeLinea = linea.split(';')
        matriz_res.append(camposDeLinea)

    # ordena los datos segun el primer elemento, osea que quedan ordenados por el tamaño de la imagen
    sort_res = Sort(matriz_res, 0)

    # saco cuantos datos hay por imagen
    cant_resultados_por_imagen = int(len(sort_res) / 8)

    x = []
    y_gray = []
    y_blur = []
    title = []

    # ciclo que recorre los resultados cortando por cada tamano de imagen
    for i in range(0, len(sort_res), cant_resultados_por_imagen):

        # me quedo solo con un tamano de imagen
        res_por_imagen = sort_res[i:i+cant_resultados_por_imagen]

        # aca separo las columnas en listas para despues plotear
        x.append(get_item(res_por_imagen, 1))
        y_gray.append(get_item(res_por_imagen, 3))
        y_blur.append(get_item(res_por_imagen, 7))
        title.append(str(res_por_imagen[0][0]))

    # arranco el subplot gray
    fig, axs = plt.subplots(2, 4)
    fig.suptitle('Escalabilidad_gray')
    axs[0, 0].plot(x[0], y_gray[0])
    axs[0, 0].set_title(title[0])
    axs[0, 1].plot(x[1], y_gray[1])
    axs[0, 1].set_title(title[1])
    axs[0, 2].plot(x[2], y_gray[2])
    axs[0, 2].set_title(title[2])
    axs[0, 3].plot(x[3], y_gray[3])
    axs[0, 3].set_title(title[3])
    axs[1, 0].plot(x[4], y_gray[4])
    axs[1, 0].set_title(title[4])
    axs[1, 1].plot(x[5], y_gray[5])
    axs[1, 1].set_title(title[5])
    axs[1, 2].plot(x[6], y_gray[6])
    axs[1, 2].set_title(title[6])
    axs[1, 3].plot(x[7], y_gray[7])
    axs[1, 3].set_title(title[7])

    plt.show()
