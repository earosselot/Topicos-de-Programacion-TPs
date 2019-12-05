# -*- coding: utf-8 -*-

# Topicos de Programacion 2019 - Trabajo Practico - Ejercicio 1 
# Grupo 1
# Perez Frasette, Maximiliano - Rosselot, Eduardo Agustin

import time
import random
import matplotlib.pyplot as plt
import numpy as np

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
            # Se agrega la tupla de la línea a la lista de tuplas completa
            tuplas.append(tuple(camposDeLinea))
    return tuplas


def distanciaMinima(l):
    """Función que partiendo de una lista de tuplas (l) devuelve el par de tuplas cuya distancia euclídea es mínima.
    Esta función utiliza fuerza bruta :@. Necesita recibir una lista de al menos dos elementos"""

    distRef = distancia(l[0],l[1]) #es una distancia de referencia.
    
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
    """Esta función es análoga a 'distanciaMinima', pero utiliza la técnica de Divide & Conquer ^.^"""
    
    #Preprocesamiento: ordenamiento de la lista l
    if algoritmo == "python":
        l.sort()
    elif algoritmo == "up":
        upSort(l)
    elif algoritmo == "merge":
        mergeSort(l)
    else:
        return "Parámetro inválido, usar 'up', 'python' ó 'merge'"
            
    #Procesamiento: busca de manera recursiva el par más cercano usando DyC.
    ParMinimo = minimaDistRec(l)
    
    return ParMinimo 


"""
FUNCIONES AUXILIARES PARA CALCULAR LA DISTANCIA
"""

def entero(a):
    """Función que convierte los numeros (que estan como string) en una lista a float"""

    for i in range(len(a)):
        a[i] = float(a[i])
    return a


def distancia(p1, p2):
    """Función que calcula y devuelve la distancia euclídea entre dos tuplas de entrada (p1 y p2)"""

    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)) ** (1/2)

"""
FUNCIONES AUXILIARES PARA ENCONTRAR EL PAR MINIMO USANDO DIVIDE & CONQUER
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
    """Función que a partir de dos listas ordenadas (l1 y l2), devuelve una lista con los elementos
    de l1 y l2 ordenados."""

    #Creo una lista vacia para guardar los elementos ordenados
    merged = []

    #ciclo que se ejecuta hasta que una de las listas no tiene elementos
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
        return par 
    
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
        dIz = distancia(minIz[0],minIz[1])
        dDer = distancia(minDer[0],minDer[1])
        
        
        #Busco posibles pares de puntos entre los grupos de izquierda y derecha
        mezcla = paresCruzados(minIz,minDer,CorteEnX,min(dIz,dDer))
        
        #Este es el paso de conquistar
        if len(mezcla) > 1: #si la longitud es mayor a 1, chequeo.
            minMezcla = distanciaMinima(mezcla)
            
            #sólo me queda elegir el par más chico
            posRes = [minIz, minDer, minMezcla]
            Res = minMezcla #tomo como referencia el par de puntos obtenidos de mezclar
            
            for i in range(len(posRes)):
                if distancia(posRes[i][0],posRes[i][1]) < distancia(Res[0],Res[1]):
                    Res = posRes[i]
            return Res
        else:
            if dIz < dDer:
                return minIz
            else:
                return minDer
            
               
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
      
    return posiblesPares
            

"""
EXPERIMENTOS DE TIEMPO
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


def experimentarAlgoritmos():
    """ Es una función que genera pares de datos y corre las funciones minimaDistancia(l) y
    de minimaDistanciaDyC(l,algoritmo). Devuelve un .txt con los tiempos de ejecución de
    ambas funciones para cada par de datos"""
    
    #Genero un set de datos 
    cant = [1000,5000,10000,15000,20000,50000]
    
    #Guardo los tiempos registrados en una matriz de 4*6.
    tiempos = np.zeros(shape = (4,6)) 
    
    #Hay un ciclo anidado para realizar el experimentos.
    
    for i in range(len(cant)): #repito para diferentes funciones                 
        for j in range(tiempos.shape[1]):   #pruebo para las diferentes sets 
            
            datos = puntosAleatorios(cant[j],2500)
            
            if i == 0:
                t0 = time.time()
                distanciaMinima(datos)
                t1 = time.time()
                tiempos[i,j] = (t1 - t0)
            elif i == 1:
                t0 = time.time()
                distanciaMinimaDyC(datos,"python")
                t1 = time.time()
                tiempos[i,j] = (t1 - t0)
            if i == 2:
                t0 = time.time()
                distanciaMinimaDyC(datos,"up")
                t1 = time.time()
                tiempos[i,j] = (t1 - t0)
            if i == 3:
                t0 = time.time()
                distanciaMinimaDyC(datos,"merge")
                t1 = time.time()
                tiempos[i,j] = (t1 - t0)
    
    return (np.savetxt("datosGrafico1.txt",tiempos)) #quiero guardar los datos en un txt

res = experimentarAlgoritmos()
                
"""
GRÁFICOS
"""

datos = listaDePuntos("datosGrafico1.txt") 
x = [1000,5000,10000,15000,20000, 50000] #Eje x, cantidad de datos
y_fb = datos[0] #Eje y, para tiempos de fuerza bruta
y_python = datos[1] #Eje y, para tiempos de DyC ordenando por python
y_upsort = datos[2] #Eje y, para tiempos de DyC ordenados por upSort
y_merge = datos[3] #Eje y, para tiempos de DyC ordenados por merge

figura = plt.figure()
plt.title("Tiempos de ejecución para algoritmos \n de diferente complejidad", fontweight = "bold")
plt.xlabel("Cantidad de puntos")
plt.ylabel("Tiempos de Ejecución (s)")
#plt.xscale("log")
plt.plot(x,y_fb, label = "Fuerza Bruta", color = "black", linewidth = 2.0, linestyle="-", marker = "o")
plt.plot(x,y_python, label = "DyC: Python", color = "green", linewidth = 3.0, linestyle="-", marker = "s")
plt.plot(x,y_upsort, label = "DyC: Upsort", color = "red", linewidth = 2.0, linestyle="-", marker = "x")
plt.plot(x,y_merge, label = "DyC: Merge", color = "blue", linewidth = 1.5, linestyle="--", marker = "*")
plt.legend(loc = "best")
plt.savefig("GraficosEj1.png")
plt.show()



"""
PRUEBA DE LAS FUNCIONES

datitos = listaDePuntos('datitos.txt')
print("Lista de Coordenadas \n",datitos,"\n")
print("Distancia minima (Fuerza Bruta) \n", distanciaMinima(datitos), "\n")
print("Ordenamiento por Upsort \n", upSort(datitos),"\n")
print('Ordenamiento por MergeSort: \n ', mergeSort(datitos),"\n")
print("Ordenamiento por Python: \n", datitos.sort(),"\n")
print("Distancia minima: D&C (Python) \n",distanciaMinimaDyC(datitos, "python"), "\n")
print("Distancia minima: D&C (mergeSort) \n",distanciaMinimaDyC(datitos, "merge"), "\n")
print("Distancia minima: D&C (UpSort) \n",distanciaMinimaDyC(datitos, "up"), "\n")    
"""



