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

def distanciaMinimaDyC(l,algoritmo):
    """Esta función es análoga a 'distanciaMinima', pero utiliza la técnica de Divide & Conquer"""
    
    #Preprocesamiento: ordenamiento de la lista l
    if algoritmo == "python":
        l.sort()
    elif algoritmo == "up":
        upSort(l)
    elif algoritmo == "merge":
        mergeSort(l)
    else:
        print("Algoritmo inválido, usar 'up', 'python' ó 'merge'")


    
#funciones para implementar upsort.
#VER (aparentemente python comparar la coordenada x por default)

def maxPos(a,b,c):
    """Busca la posición del elemento más grande de una lista entre los índices b y c"""
    sublista = a[b:(c+1)] #(c+1) porque quiero incluir c
    pos = 0
    maximo = sublista[0]
    for i in range(len(sublista)):  #VER (uso fuerza bruta, no sé si está bien)
        if maximo <= sublista[i]:
            maximo = sublista[i]
            pos = i
    return pos

def upSort(l): #es el código que Esteban dió en la teórica
    """Ordena una lista l utilizando la técnica de upsort """
    actual = len(l) - 1
    m = 0
    while actual > 0:
        m = maxPos(l,0,actual)
        a[m],a[actual] = a[actual],a[m]
        actual -= 1

#funciones para implementar merge
def dividirEnDos(l):
    """Divide a la lista l en dos mitades, no necesariamente iguales"""
    if len(l) == 2 or len(l) == 1:
        return l
    else:
        sublist1 = l[:int((len(l)/2))] 
        sublist2 = l[int((len(l)/2)):]
    return sublist1, sublist2
        

def mergeSort(l):
    """Ordena una lista l utilizando la técnica de merge"""
    if len(l) == 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            l[0],l[1] = l[1],l[0]
        return l
    else:
        listas = dividirEnDos(l)
        print(mergeSort(listas[0]))
        print(mergeSort(listas[1]))
        
        



a = listaDePuntos('datitos.txt')
print("Lista de Coordenadas \n",a,"\n")
print("Distancia minima \n", distanciaMinima(a),"\n")
mergeSort(a)
#print(distancia(a[0], a[1]))
