# -*- coding: utf-8 -*-
import ast
import random
import sys

# Cambio el limite de recursion para que llegue a resolver los laberintos
sys.setrecursionlimit(3000)


class Laberinto(object):
    """"Vamos de definir funciones para crear un laberinto.
    La función init se inicializa siempre que se llama a la clase Laberinto """

    def __init__(self, parent=None):
        self.parent = parent
        self.laberinto = []
        self.PosRata = (0, 0)
        self.PosQueso = (0, 0)
        self.shape = (0, 0)
        # self._res_lab: matriz de NxMx2, donde la capa 0, guarda las pocisiones visitadas y la capa 1 guarda el camino
        # actual. Se marca True si es parte del camino actual/visitada y False en caso contrario.
        self._res_lab = []
        # self._camino: lista de tuplas que forman parte del camino actual
        self._camino = []
        # self._cantidad_movimientos: contador de todos los movimientos que hizo la rata
        self._cantidad_movimientos = 0

    # INTERFAZ (metodos publicos)

    def cargar(self, fn):
        """"Carga un laberinto a partir de un archivo .lab"""
        listaDeCeldas = []
        with open(fn, 'r') as entrada:
            corch1 = '['        # creo unas cadenas para poder rellenar el ppio y el final de los split
            corch2 = ']'
            next(entrada)                                               # saltea la primera linea
            for linea in entrada:                                       # recorre la entrada (desde la segunda linea)
                linea = linea.strip('\n').lstrip('[').rstrip(']')       # recorte del \n y del corchete inicial y final
                fila = []                                               # vacia la fila para cada itereacion
                for casillero in linea.split(']['):     # divide la linea donde abren y cierran corchetes
                    fila.append(ast.literal_eval(corch1+casillero+corch2))   # ast.lit pasa un str a lista
                listaDeCeldas.append(fila)      # agrego la fila al laberinto
        self.laberinto = listaDeCeldas
        # obtengo el tamano del laberinto y seteo las posiciones del queso y la rata
        m = len(self.laberinto)
        n = len(self.laberinto[1])
        self.shape = (m, n)
        self.setPosicionRata(0, 0)
        self.setPosicionQueso(self.shape[0] - 1, self.shape[1] - 1)
        self._notescapes()
        self.resetear()
        self._cantidad_movimientos = 0

    def tamano(self):
        """Metodo que devuelve una tupla con la cantidad de filas y columnas"""
        return self.shape

    def resetear(self):
        """metodo que limpia el laberinto"""
        self._res_lab = []
        for i in range(self.shape[0]):
            fila = []
            for j in range(self.shape[1]):
                fila.append({'visitada': False, 'caminoActual': False})
            self._res_lab.append(fila)

    def getPosicionRata(self):
        """metodo que devuelve una tupla con las coordenadas de la rata"""
        return self.PosRata

    def getPosicionQueso(self):
        """metodo que devuelve una tupla con las coordenadas del queso"""
        return self.PosQueso

    def setPosicionRata(self, i, j):
        """Metodo que posiciona a la rata en el casillero (i, j) del laberinto y devuelve True si el seteo es posible.
        Si no, devuelve False y deja la rata en su lugar"""
        if i < self.shape[0] and j < self.shape[1]:
            self.PosRata = (i, j)
            return True
        else:
            return False

    def setPosicionQueso(self, i, j):
        """Metodo que posiciona el queso en el casillero (i, j) del laberinto y devuelve True si el seteo es posible.
        Si no, devuelve False y deja el queso en su lugar"""
        if i < self.shape[0] and j < self.shape[1]:
            self.PosQueso = (i, j)
            return True
        else:
            return False

    def esPosicionRata(self, i, j):
        """Metodo que devuelve True si el par ordenado determinado por (i, j) corresponde a la posición de la rata,
        False en caso contrario."""
        if self.PosRata == (i, j):
            return True
        else:
            return False

    def esPosicionQueso(self, i, j):
        """Metodo que devuelve True si el par ordenado determinado por (i, j) corresponde a la posición del queso,
        False en caso contrario."""
        if self.PosQueso == (i, j):
            return True
        else:
            return False

    def get(self, i, j):
        """Metodo que devuelve una lista con 4 elementos booleanos, que indican si hay pared o no en cada uno
        de los 4 bordes de la celda ubicada en la fila i, columna j. El orden en el que deben aparecer los bordes es el
        siguiente: Izquierda, Arriba, Derecha, Abajo"""
        celda_bool = []
        for elem in self.laberinto[i][j]:
            if elem == 0:
                celda_bool.append(False)
            else:
                celda_bool.append(True)
        return celda_bool

    def getInfoCelda(self, i, j):
        """Metodo que devuelve un diccionario con información acerca de la celda ubicada en la posición (i, j).
        El diccionario tiene dos claves: visitada y caminoActual. La clave visitada es un booleano que
        indica si la celda fue visitada por el backtracking, mientras que caminoActual indica si es parte del camino
        actual que está siendo probado por el backtracking"""
        return self._res_lab[i][j]

    def resuelto(self):
        """devuelve True si el laberinto está resuelto, es decir, si la posición de la rata es la misma que
        la del queso, y False en otro caso"""
        return self.PosQueso == self.PosRata

    def resolver(self):
        """Metodo que resuelve el laberinto por backtraking"""

        # RESOLUCION DEL LABERINTO (en numero las decisiones posibles y en letras las opciones segun el caso):

        # 1. Lluegue al queso ?
        #     1-a: si -> resuelto FIN
        if self.resuelto():
            print("resuleto en %i movimientos" % self._cantidad_movimientos)
            return True
        #     1-b: no ->
        else:
            # guardo la posicion actual porque se usa mucho y el codigo queda mas entendible
            i = self.PosRata[0]
            j = self.PosRata[1]
            # posible: lista booleano, si es True el movimiento hacia ese lugar es valido [izq, arr, der, ab]
            posible = self._and_listas(self._not_lista(self.get(i, j)), self._not_lista(self._getVisita(i, j)))

        # 2. hay lugares para moverse (sin paredes y sin visita)?
        #   2-a: no -> no tiene solucion FIN
            if self._todo_False(posible):
                print("NO resuleto en %i movimientos" % self._cantidad_movimientos)
                return False
        #     2-b: si ->
            else:

        # 3. alguno de los lugares para moverse estan inexplorados? (posibles = True y camino = False)
                # self._get_camino(i, j) -- True en los que son parte del camino
                # posible -- True para donde se puede ir
                # inexplorado: lista de 4 elementos, True en las direcciones inexploradas
                inexplorado = self._and_listas(posible, self._not_lista(self._getCamino(i, j)))
                # pos_inexploradas: lista de los indices donde inexplorado es True (o vacia, si no hay Trues)
                pos_inexploradas = self._pos_true(inexplorado)
        #   3-a: si -> sigo por ese (mover + marcar camino actual)
                if len(pos_inexploradas) > 0:
                    movimiento = random.choice(pos_inexploradas)    # elijo uno al azar entre los movimientos
                    self._res_lab[i][j]["caminoActual"] = True                   # marco el lugar actual como camino
                    self._camino.append((i, j))                     # guardo en el _camino el lugar actual
                    self._mover(movimiento, i, j)                   # muevo la rata
                    self._cantidad_movimientos += 1                 # contador de movimientos(para estimar el rec.limit)
                    self._redibujar()
                    self.resolver()                                 # llamada recursiva
        #   3-b: no -> vuelvo (mover + marcar visita + desmarcar camino actual)
                else:
                    self.setPosicionRata(self._camino[-1][0], self._camino[-1][1])    # vuelvo al ultimo lugar
                    self._cantidad_movimientos += 1
                    self._res_lab[i][j]["visitada"] = True                    # marco el camino como visitado
                    self._res_lab[i][j]["caminoActual"] = False               # lo desmarco como camino actual
                    self._camino.pop(-1)                            # elimino la casilla del _camino
                    self._redibujar()
                    self.resolver()                                 # llamada recursiva

    # AUXILIARES (metodos privados)

    def _mover(self, movimiento, i, j):
        """mueve la rata desde el casillero (i, j) al casillero que indica movimiento
        0: izquierda, 1: arriba, 2: derecha, 3(else): abajo"""
        if movimiento == 0:
            self.setPosicionRata(i, j-1)
        elif movimiento == 1:
            self.setPosicionRata(i-1, j)
        elif movimiento == 2:
            self.setPosicionRata(i, j+1)
        elif movimiento == 3:
            self.setPosicionRata(i+1, j)

    def _getVisita(self, i, j):
        """Metodo que segun una coordenada (i,j) devuelve una lista booleana en funcion si las casillas adyacentes
        fueron o no visitadas con el siguiente arreglo visita = [izquierda, arriba, derecha, abajo]"""
        visita = [False, False, False, False]
        # hacia iquierda
        if j != 0:
            vis = self._res_lab[i][j-1]["visitada"]
            visita[0] = vis
        # hacia derecha
        if j != self.shape[1] - 1:
            vis = self._res_lab[i][j+1]["visitada"]
            visita[2] = vis
        # hacia arriba
        if i != 0:
            vis = self._res_lab[i-1][j]["visitada"]
            visita[1] = vis
        # hacia abajo
        if i != self.shape[0] - 1:
            vis = self._res_lab[i+1][j]["visitada"]
            visita[3] = vis
        return visita

    def _getCamino(self, i, j):
        """Metodo que segun una coordenada (i,j) devuelve una lista booleana en funcion si las casillas adyacentes
        son o no parte del camino actual con el siguiente arreglo camino = [izquierda, arriba, derecha, abajo]"""
        camino = [False, False, False, False]
        # hacia iquierda
        if j != 0:
            camino[0] = self._res_lab[i][j-1]["caminoActual"]
        # hacia derecha
        if j != self.shape[1] - 1:
            camino[2] = self._res_lab[i][j+1]["caminoActual"]
        # hacia arriba
        if i != 0:
            camino[1] = self._res_lab[i-1][j]["caminoActual"]
            # hacia abajo
        if i != self.shape[0] - 1:
            camino[3] = self._res_lab[i+1][j]["caminoActual"]
        return camino

    def _notescapes(self):
        """Metodo que cierra las salida de emergencia -.-"""
        for i in range(self.shape[0]):
            self.laberinto[i][0][0] = 1
            self.laberinto[i][self.shape[1]-1][2] = 1
        for j in range(self.shape[1]):
            self.laberinto[0][j][1] = 1
            self.laberinto[self.shape[0]-1][j][3] = 1

    def _pos_true(self, l1):
        """devuelve una lista con las posiciones de la lista que tienen True"""
        trues = []
        for i in range(len(l1)):
            if l1[i]:
                trues.append(i)
        return trues

    def _todo_False(self, l1):
        """devuelve True si todos los elementos de la lista l1 son False"""
        i = 0
        while i < len(l1) and l1[i] is False:
            i += 1
        if i == len(l1):
            return True
        else:
            return False

    def _and_listas(self, l1, l2):
        """hace un and elemento a elemento entre dos listas del mismo tamano y devuelve una lista con los resultados"""
        list_and = []
        for i in range(len(l1)):
            list_and.append(l1[i] and l2[i])
        return list_and

    def _not_lista(self, l1):
        """aplica not a todos los elementos de una lista l1 y devuelve la lista negada"""
        for i in range(len(l1)):
            l1[i] = not (l1[i])
        return l1

    def _redibujar(self):
        if self.parent is not None:
            self.parent.update()
