# Topicos de Programacion 2019 - Trabajo Practico - Ejercicio 1 #
# Grupo N ####
# Perez Frastte, Maximiliano - Rosselot, Eduardo Agustin

def entero(a):
    """funcion que convierte los numeros (que estan como string) en una lista a float"""

    for i in range(len(a)):
        a[i] = float(a[i])
    return a


def listaDePuntos(fn):
    """Función que abre el archivo fn y devuelve una lista con las tuplas separadas por espacios del archivo"""

    # Abre los archivos de entrada (en modo r:Read)
    with open(fn, 'r') as entrada:

        tuplas = []   # Aquí nos vamos a guardar todas las tuplas del archivo de entrada

        for linea in entrada:
            linea = linea.strip('\n')         # Elimina el salto de línea del final
            camposDeLinea = linea.split(' ')  # Se parte la cadena de la línea entera y se genera una lista
            entero(camposDeLinea)
            # Se agrega la tupla de  la línea a la lista de tuplas completa
            tuplas.append(tuple(camposDeLinea))
    return tuplas


def distancia(x, y):
    """Función que calcula y devuelve la distancia euclídea entre dos tuplas de entrada (x e y)"""

    return (((x[0] - y[0])**2) + ((x[1] - y[1])**2)) ** (1/2)


def distanciaMinima(l):
    """Función que partiendo de una lista de tuplas (l) devuelve el par de tuplas cuya distancia euclídea es mínima.
    Esta función utiliza fuerza bruta :@ """

    distancias = []

    for i in range(len(l) - 1):
        for j in range(i + 1, len(l) - 1):
            distancias.append(distancia(l[i], l[j]))
    return min(distancias)


a = listaDePuntos('datitos.txt')
print(a)
print(distanciaMinima(a))
print(distancia(a[0], a[1]))
