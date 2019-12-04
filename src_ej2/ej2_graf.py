# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def Sort(sub_li, elem):
    """ordena la lista de listas segun un elemento pasado como parametro (elem)"""

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
        res_por_imagen = sort_res[i:i + cant_resultados_por_imagen]

        # aca separo las columnas en listas para despues plotear
        x.append(get_item(res_por_imagen, 1))
        y_gray.append(np.array(get_item(res_por_imagen, 3)) * 1000)
        y_blur.append(np.array(get_item(res_por_imagen, 7)) * 1000)
        title.append(str(res_por_imagen[0][0]))


    # arranco el subplot gray
    fig, axs = plt.subplots(2, 4, figsize=(10,10))
    fig.suptitle('Escalabilidad (filtro gray)', fontweight = "bold", fontsize = 18)
    fig.text(0.5, 0.04, 'Número de threads', ha='center', fontsize = 15)
    fig.text(0.04, 0.5, 'Tiempo (ms)', va='center', rotation='vertical', fontsize = 15)


    # genera los subplots
    for i in range(axs.shape[0]):
        for j in range(axs.shape[1]):
            axs[i, j].plot(x[(4 * i) + j], y_gray[(4 * i) + j])
            axs[i, j].set_title(title[(4 * i) + j])
            axs[i, j].set_xticks([2, 4, 6, 8, 10, 12, 14, 16])
            # plt.xticks([2, 4, 6, 8, 10, 12, 14, 16])
    plt.subplots_adjust(wspace=0.3)
    plt.show()

    # Figura 
    fig1, axs = plt.subplots(2, 4, figsize=(10,10))
    fig1.suptitle('Escalabilidad (filtro blur)', fontweight = "bold", fontsize = 18)
    fig1.text(0.5, 0.04, 'Número de threads', ha='center', fontsize = 15)
    fig1.text(0.04, 0.5, 'Tiempo de ejecucion (ms)', va='center', rotation='vertical', fontsize = 15)

    # genera los subplots
    for i in range(axs.shape[0]):
        for j in range(axs.shape[1]):
            axs[i, j].plot(x[(4 * i) + j], y_blur[(4 * i) + j])
            axs[i, j].set_title(title[(4 * i) + j])
            axs[i, j].set_xticks([2, 4, 6, 8, 10, 12, 14, 16])
            # plt.xticks([2, 4, 6, 8, 10, 12, 14, 16])
    
    plt.subplots_adjust(wspace=0.5)
    plt.show()