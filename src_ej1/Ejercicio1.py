# -*- coding: utf-8 -*-
# Topicos de Programacion 2019 - Trabajo Practico - Ejercicio 1 #
# Grupo N ####
# Perez Frasette, Maximiliano - Rosselot, Eduardo Agustin

import time
import random
import matplotlib.pyplot as plt

"""
FUNCIONES PRINCIPALES
"""
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


def distanciaMinima(l):
    """Función que partiendo de una lista de tuplas (l) devuelve el par de tuplas cuya distancia euclídea es mínima.
    Esta función utiliza fuerza bruta :@ """

    distRef = distancia(l[0],l[1]) #es mi distancia de referencia.
    
    if len(l) == 2:
        return l
    
    else:    
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):  
                d = distancia(l[i],l[j])
                if d <= distRef:
                    distRef = d
                    par = [l[i],l[j]]
    return par
    


def distanciaMinimaDyC(l, algoritmo):
    """Esta función es análoga a 'distanciaMinima', pero utiliza la técnica de Divide & Conquer"""
    
    #Preprocesamiento: ordenamiento de la lista l
    if algoritmo == "python":
        l.sort()
    elif algoritmo == "up":
        upSort(l)
    elif algoritmo == "merge":
        mergeSort(l)
    else:
        print("Parámetro inválido, usar 'up', 'python' ó 'merge'")
            
    #ACÁ VA LA FUNCIÓN RECURSIVA


"""
FUNCIONES AUXILIARES PARA CALCULAR LA DISTANCIA
"""

def entero(a):
    """funcion que convierte los numeros (que estan como string) en una lista a float"""

    for i in range(len(a)):
        a[i] = float(a[i])
    return a


def distancia(p1, p2): #lo cambié porque me confundian los nombre jeje
    """Función que calcula y devuelve la distancia euclídea entre dos tuplas de entrada (x e y)"""

    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** (1/2)

"""
FUNCIONES AUXILIARES PARA CALCULAR LA DISTANCIA USANDO DIVIDE & CONQUER
"""

#funciones auxiliares para implementar upsort
def maxPos(a, b, c):
    """Busca la posición del elemento más grande de una lista entre los índices b y c"""

    sublista = a[b:(c+1)]   #(c+1) porque quiero incluir c
    pos = 0
    maximo = sublista[0]
    for i in range(1, len(sublista)):
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
    return l

#funciones auxiliares para implementar mergeSort

def dividirEnDos(l):
    """Divide a la lista l en dos mitades, si la lista es mayor a 2.
    Si tiene cantidad impar de elementos, la primer mitad es mas chica.
    El último elemento de la lista resultado es la coordenada de corte"""
    if len(l) < 3:
        return l
    else:
        sublist1 = l[:int((len(l)/2))] #mitad izquierda
        sublist2 = l[int((len(l)/2)):] #mitad derecha
        
        Delta = (sublist2[0][0] - sublist1[len(sublist1)-1][0])/2
        EjeDeCorte = Delta + sublist1[len(sublist1)-1][0]
    return sublist1, sublist2, EjeDeCorte


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

#Funciones auxiliares para resolver distanciaMinimaDyC

def minimaDistRec(l):
    """Devuelve el par de puntos más cercanos. Necesita una lista ordenada en x """
    
    #Planteo el caso base
    if len(l) <= 3:  #si tengo 3 o menos puntos, uso fuerza bruta
        par = distanciaMinima(l)
        dist = distancia(par[0],par[1])
        #Le pido de devuelve el par (es lo que me interesa) y la distancia (voy a necesitarla para calcular)
        return par,dist 
    
    else:
        #divido la lista en dos mitades (izquierda y derecha)
        mitades = dividirEnDos(l)
        
        #separo mis mitades en dos listas y guardo el punto medio
        mIz = mitades[0]
        mDer = mitades[1]
        CorteEnX = mitades[2]
        
        #hago el paso recursivo      
        minIz = minimaDistRec(mIz)
        minDer = minimaDistRec(mDer)         
        print(minIz)
        print(minDer)               
        #Busco posibles pares de puntos entre los grupos de izquierda y derecha
        mezcla = paresCruzados(minIz[0],minDer[0],CorteEnX,min(minIz[1],minDer[1]))
        print(mezcla)
        if len(mezcla) > 1: #si la longitud es mayor a 1, chequeo.
            minMezcla = distanciaMinima(mezcla)
            
            #sólo me queda elegir el par más chico
            posRes = [minIz[0], minDer[0], minMezcla]
            Res = minMezcla #tomo como referencia el par de puntos obtenidos de mezclar
            
            for i in range(len(posRes)):
                if distancia(posRes[i][0],posRes[i][1]) < distancia(Res[0],Res[1]):
                    Res = posRes[i]
            return Res
        else:
            if minIz[1] < minDer[1]:
                return minIz[0]
            else:
                return minDer[0]
            
    
           
def paresCruzados(l1,l2,x,dist):
    """Esta función busca los pares que quedan por resolver. Es el paso de
    combinar"""
    posiblesPares = []
    for i in range(len(l1)):
        if  (x - l1[i][0]) <= dist:
            posiblesPares.append(l1[i])
    for i in range(len(l2)):
        if (l2[i][0] - x) <= dist:
            posiblesPares.append(l2[i])
    
    if len(posiblesPares) != 0:
        return posiblesPares
    else:
        return dist
            

"""
PRUEBA DE LAS FUNCIONES
"""
datitos = listaDePuntos('datitos.txt')
#print("Lista de Coordenadas \n",datos,"\n")
#print("Distancia minima (Fuerza Bruta) \n", distanciaMinima(datos), "\n")
#print("Ordenamiento por Upsort \n", upSort(datos),"\n")
#print('Ordenamiento por MergeSort: \n ', mergeSort(datos),"\n")
#print("Ordenamiento por Python: \n", datos.sort(),"\n")
#print("Distancia minima: D&C (Python) \n",distanciaMinimaDyC(datos, "python"), "\n")
#print("Distancia minima: D&C (mergeSort) \n",distanciaMinimaDyC(datos, "merge"), "\n")
#print("Distancia minima: D&C (UpSort) \n",distanciaMinimaDyC(datos, "up"), "\n")

"""
PRUEBA CON DIFERENTES DATOS
"""
def puntosAleatorios(a,b):
    """Genera una lista de longitud a con pares de números aleatorios entre
    -b y b"""
    miSet = []
    for i in range(a):
        if random.random() < 0.5:
            b = b*(-1)
            miSet.append((round((random.random()*b),2),round((random.random()*b),2)))
        else:
            miSet.append((round((random.random()*b),2),round((random.random()*b),2)))
            
    return miSet

#ParesDiez = puntosAleatorios(10,100)
#ParesCien = puntosAleatorios(100,1000)
#ParesMil = puntosAleatorios(1000,10000)
#ParesCincoMil = puntosAleatorios(5000,100000)


def medir_tiempos(fn,*args):
    """Mide los tiempos de ejecuciòn de la función fn"""
    t0 = time.time()
    fn(*args)
    tf = time.time()
    
    return (tf-t0)
  
    
"""
TiemposFuerzaBruta = []

TiemposFuerzaBruta.append(medir_tiempos(distanciaMinima,ParesDiez))
TiemposFuerzaBruta.append(medir_tiempos(distanciaMinima,ParesCien))
TiemposFuerzaBruta.append(medir_tiempos(distanciaMinima,ParesMil))
TiemposFuerzaBruta.append(medir_tiempos(distanciaMinima,ParesCincoMil))

print("Dist Min:",distanciaMinima(ParesCien))
print(TiemposFuerzaBruta)


TiemposDyCM = []

TiemposDyCM.append(medir_tiempos(distanciaMinimaDyC,ParesDiez,"merge"))
TiemposDyCM.append(medir_tiempos(distanciaMinimaDyC,ParesCien,"merge"))
TiemposDyCM.append(medir_tiempos(distanciaMinimaDyC,ParesMil,"merge"))
TiemposDyCM.append(medir_tiempos(distanciaMinimaDyC,ParesCincoMil,"merge"))

print("Dist Min:", distanciaMinima(ParesCien))
print(TiemposDyCM)

TiemposDyCU = []

TiemposDyCU.append(medir_tiempos(distanciaMinimaDyC,ParesDiez,"up"))
TiemposDyCU.append(medir_tiempos(distanciaMinimaDyC,ParesCien,"up"))
TiemposDyCU.append(medir_tiempos(distanciaMinimaDyC,ParesMil,"up"))
TiemposDyCU.append(medir_tiempos(distanciaMinimaDyC,ParesCincoMil,"up"))

print("Dist Min:", distanciaMinima(ParesCien))
print(TiemposDyCU)
"""


