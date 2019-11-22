# import imfilters
# from scipy import misc
# import scipy
import imageio
import numpy as np


def gray_filter(img):
    """filtro que hace una transformacion de una imagen color a una en escala de grises con ciertos valores"""

    # genero una matriz de 0 del tamaño de la imagen
    x = img.shape[0]
    y = img.shape[1]
    res = np.zeros([x, y])

    # hago el filtrado
    res = 0.3 * img[:, :, 0] + 0.6 * img[:, :, 1] + 0.11 * img[:, :, 2]
    return res


def blur_filter(img):
    """Filtro que recibe una imagen matriz en grises y devuelve una matriz difuminada"""

    # genero una matriz de 0 del tamaño de la imagen
    filas = img.shape[0]
    col = img.shape[1]
    res = np.zeros([filas, col])

    # los dos for anidados recorren toda la imagen excepto lo bordes
    for i in range(1, filas - 1):
        for j in range(1, col - 1):
            # este calculo ganera el valor promedio que requiere el blur
            res[i, j] = (img[i - 1, j] + img[i + 1, j] + img[i, j - 1] + img[i, j + 1]) / 4
    return res



im = imageio.imread('MaleLionNamibia.jpg')
print(im.shape)
res = gray_filter(im)
print(res)
