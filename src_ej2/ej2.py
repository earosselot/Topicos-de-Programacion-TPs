import sys
import os
import imageio
import numpy as np
from numba import jit
import time


# @jit(parallel=True)
def gray_filter(img):
    """filtro que hace una transformacion de una imagen color a una en escala de grises con ciertos valores"""

    # genero una matriz de 0 del taman-o de la imagen
    x = img.shape[0]
    y = img.shape[1]
    gray = np.zeros((x, y))

    # hago el filtrado
    gray = 0.3 * img[:, :, 0] + 0.6 * img[:, :, 1] + 0.11 * img[:, :, 2]
    return gray


# @jit(parallel=True)
def blur_filter(img):
    """Filtro que recibe una imagen matriz en grises y devuelve una matriz difuminada"""

    # genero una matriz de 0 del taman-o de la imagen
    filas = img.shape[0]
    col = img.shape[1]
    res = np.zeros((filas, col))

    # los dos for anidados recorren toda la imagen excepto lo bordes
    for i in range(1, filas - 1):
        for j in range(1, col - 1):
            # este calculo ganera e l valor promedio que requiere el blur
            res[i, j] = (img[i - 1, j] + img[i + 1, j] + img[i, j - 1] + img[i, j + 1]) / 4
    # img_uint8 = res.astype(np.uint8)
    # imageio.imwrite('out_jit.jpg', img_uint8)
    return res


def medirTiempos(fn, *args):
    """devuelve el tiempo, en segundos, que tarda en ejecutarse la funcion(fn) con los argumentos (*args)"""

    t0 = time.time()
    fn(*args)
    t1 = time.time()
    return t1 - t0


def getfilenames(path):
    """funcion que devuelve una lista con las rutas de los archivos del tipo requerido y su path local
    formato path (str): 'path/al/archivo/*.tipo' """

    ftype = path.split(".")[-1]
    folder = path.split("*")[0]
    data_list = []

    for i in os.listdir(folder):
        if ftype in i.split(".")[-1]:
            data_list.append(folder+i)
    return data_list


def main(argumentos):

    arch_entrada = sorted(getfilenames(argumentos[0]))
    threads = str(argumentos[1])
    veces = int(argumentos[2])
    tiempos = [[], []]

    # os.environ["NUMBA_NUM_THREADS"] = threads
    for p in range(veces):

        for image in arch_entrada:

            im = imageio.imread(image)

            tiempos[0].append((medirTiempos(gray_filter, im)))

            gray = gray_filter(im)
            tiempos[1].append(medirTiempos(blur_filter, gray))

        with open('resultados.csv', 'a') as file:
            for i in range(len(arch_entrada)):
                # guardo en tam_imagen el taman-o de la imagen
                tam_imagen = arch_entrada[i].split("_")[2].split(".")[0]
                file.write("%s; %i; %f; %f\n" % (tam_imagen, int(threads), tiempos[0][i], tiempos[1][i]))
        print('a')

if __name__ == "__main__":

    # if len(sys.argv) < 4:
    #     print("")
    #     sys.exit(1)

    main(sys.argv[1:])
