# Topicos de Programacion 2019 - Trabajo Practico - Ejercicio 1 #
# Grupo N ####
# Perez Frasette, Maximiliano - Rosselot, Eduardo Agustin

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


def distanciaMinimaDyC(l, algoritmo):
    """Esta función es análoga a 'distanciaMinima', pero utiliza la técnica de Divide & Conquer"""
    
    #Preprocesamiento: ordenamiento de la lista l
    if algoritmo == "python":
        l.sort()
    elif algoritmo == "up":
        upSort(l)
    elif algoritmo == "merge":
        mergeSort(l)
    elif algoritmo == "ordenada":
        pass #significa que la lista ya está ordenada
    else:
        print("Algoritmo inválido, usar 'up', 'python' ó 'merge'")
            
    #divido la lista ordenada
    sublistas = dividirEnDos(l)
    
    #busco recursivamente la distancia minima (INCOMPLETO)
    if len(l) == 2:
        return distancia(l[0],l[1])
    else:
        return distanciaMinimaDyC(sublistas[0],"ordenada"), distanciaMinimaDyC(sublistas[1],"ordenada")
    
    
    

    
#funciones para implementar upsort.
#VER (aparentemente python comparar la coordenada x por default)


def maxPos(a, b, c):
    """Busca la posición del elemento más grande de una lista entre los índices b y c"""

    sublista = a[b:(c+1)]   #(c+1) porque quiero incluir c
    pos = 0
    maximo = sublista[0]
    for i in range(1, len(sublista)):      #VER (uso fuerza bruta, no sé si está bien)
        if maximo < sublista[i]:
            maximo = sublista[i]
            pos = i
    return pos


def upSort(l): # es el código que Esteban dió en la teórica
    """Ordena una lista l utilizando la técnica de upsort """

    actual = len(l) - 1
    m = 0
    while actual > 0:
        m = maxPos(l, 0, actual)
        l[m], l[actual] = l[actual], l[m]
        actual -= 1


#funciones para implementar merge sort

def dividirEnDos(l):
    """Divide a la lista l en dos mitades, si la lista es mayor a 2.
    Si tiene cantidad impar de elementos, la primer mitad es mas chica"""

    if len(l) < 3:
        return l
    else:
        sublist1 = l[:int((len(l)/2))] 
        sublist2 = l[int((len(l)/2)):]
    return sublist1, sublist2


def merge(l1, l2):
    """funcion que a partir de dos listas ordenadas (l1 y l2), devuelve una lista con los elementos
    de l1 y l2 ordenados."""

    # creo una lista vacia para guardar los elementos ordenados
    merged = []

    # ciclo que se ejecuta hasta que una de las listas no tiene elementos
    while len(l1) > 0 and len(l2) > 0:
        # estos if comparan los primeros elementos de la lista, guardan el menor en la lista ordenada,
        # y lo eliminan de la lista original (para que el bucle termine)
        if l1[0] <= l2[0]:
            merged.append(l1[0])
            l1.pop(0)
        else:
            merged.append(l2[0])
            l2.pop(0)

    # pone al final de la lista ordenada los elementos restantes de la lista que no se vació (y lo devuelve)
    if len(l1) > 0:
        return merged + l1
    else:
        return merged + l2


def mergeSort(l):
    """Ordena una lista l utilizando la técnica de merge"""

    if len(l) == 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        return l
    else:
        lista_dividida = dividirEnDos(l)
        return merge(mergeSort(lista_dividida[0]), mergeSort(lista_dividida[1]))





datos = listaDePuntos('datitos.txt')
print(datos,"\n")
print("Lista de Coordenadas \n",datos,"\n")
print("Distancia minima \n", distanciaMinima(datos), "\n")
print('mergeSort: ', mergeSort(datos),"\n")
print(distanciaMinimaDyC(datos, "python"), "\n")
#print(distancia(a[0], a[1]))
