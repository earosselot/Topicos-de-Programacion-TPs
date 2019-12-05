# -*- coding: utf-8 -*-

# Topicos de Programacion 2019 - Trabajo Practico - Ejercicio 2 
# Grupo 1
# Perez Frasette, Maximiliano - Rosselot, Eduardo Agustin

import sys
import os
import imageio
import numpy as np
# from numba import jit
import time
import statistics as st


def medirTiempos(fn, *args):
    """devuelve el tiempo, en segundos, que tarda en ejecutarse la funcion(fn) con los argumentos (*args)"""

    t0 = time.time()
    fn(*args)
    t1 = time.time()
    return t1 - t0


#@jit(parallel=True)
def gray_filter(img):
    """filtro que hace una transformacion de una imagen color a una en escala de grises con ciertos valores"""

    # genero una matriz de 0 del taman-o de la imagen
    x = img.shape[0]
    y = img.shape[1]
    gray = np.zeros((x, y))

    # hago el filtrado
    gray = 0.3 * img[:, :, 0] + 0.6 * img[:, :, 1] + 0.11 * img[:, :, 2]
    return gray


#@jit(parallel=True)
def blur_filter(img):
    """Filtro que recibe una imagen matriz en grises y devuelve una matriz difuminada"""

    # genero una matriz de 0 del taman-o de la imagen
    filas = img.shape[0]
    col = img.shape[1]
    res = np.zeros((filas, col))

    # los dos for anidados recorren toda la imagen excepto lo bordes
    for i in range(1, filas - 1):
        for j in range(1, col - 1):
            # este calculo genera el valor promedio que requiere el blur
            res[i, j] = (img[i - 1, j] + img[i + 1, j] + img[i, j - 1] + img[i, j + 1]) / 4
    
    # img_uint8 = res.astype(np.uint8)
    # imageio.imwrite('out_jit.jpg', img_uint8)
    return res


def getfilenames(path):
    """funcion que devuelve una lista con las rutas de los archivos del tipo requerido y su path local.
    formato path (str): 'path/al/archivo/*.tipo' """

    ftype = path.split(".")[-1]
    folder = path.split("*")[0]
    data_list = []

    for i in os.listdir(folder):
        if ftype in i.split(".")[-1]:
            data_list.append(folder + i)
    return data_list


def main(argumentos):
    arch_entrada = sorted(getfilenames(argumentos[0]))
    threads = str(argumentos[1])
    veces = int(argumentos[2])
    salida = argumentos[3]
    tiempos = [[], []]

    for image in arch_entrada:
        im = imageio.imread(image)

        for p in range(veces):

            tiempos[0].append((medirTiempos(gray_filter, im)))

            gray = gray_filter(im)
            tiempos[1].append(medirTiempos(blur_filter, gray))

        with open(salida, 'a') as file:
            tam_imagen = image.split("_")[2].split(".")[0]
            file.write("%s; %i; %i; %f; %f; %f; %f; %f; %f; %f; %f\n" % (tam_imagen, int(threads), veces,
                                                                        st.mean(tiempos[0]), st.stdev(tiempos[0]),
                                                                        min(tiempos[0]), max(tiempos[0]),
                                                                        st.mean(tiempos[1]), st.stdev(tiempos[1]),
                                                                        min(tiempos[1]), max(tiempos[1])))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print('''Se necesitan 5 argumentos: \n
        "path/a/archivos/*.extension" "# de threads" #_de_repeticiones "arch_salida"\n
        ej: python ej2.py "im/*.jpg" "10" 100 "salida.csv''')
        sys.exit(1)

    main(sys.argv[1:])
