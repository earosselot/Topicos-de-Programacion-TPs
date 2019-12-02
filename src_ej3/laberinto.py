# -*- coding: utf-8 -*-
import ast
import numpy as np


class Laberinto(object):
    """"Vamos de definir funciones para crear un laberinto.
    La función init se inicializa siempre que se llama a la clase Laberinto """

    def __init__(self, parent=None):
        self.parent = parent
        self.laberinto = np.array([])
        self.PosRata = (0, 0)
        self.PosQueso = (0, 0)
        self.shape = [0, 0]
        self.res_lab = []    # matriz de NxMx2, donde la capa 0, guarda las pocisiones visitadas y la capa
                                        # 1 guarda el camino actual. con 1 si es parte del camino actual/visitada y
                                        # 0 en caso contrario

    # interfaz (metodos publicos)

    def cargar(self, fn):
        """"Carga un laberinto a partir de un archivo .lab"""
        listaDeCeldas = []
        with open(fn, 'r') as entrada:
            corch1 = '['        # creo unas cadenas para poder rellenar el ppio y el final de los split
            corch2 = ']'
            next(entrada)       # saltea la primera linea
            for linea in entrada:       # recorre la entrada (desde la segunda linea)
                linea = linea.strip('\n').lstrip('[').rstrip(']')       # recorte del \n y del corchete inicial y final
                fila = []               # vacia la fila para cada itereacion
                for casillero in linea.split(']['):     # divide la linea donde abren y cierran corchetes
                    fila.append(ast.literal_eval(corch1+casillero+corch2))   # ast.lit pasa un str a lista
                listaDeCeldas.append(fila)  # agrego la fila al laberinto
        self.laberinto = np.array(listaDeCeldas)
        # obtengo el tamano del laberinto y seteo las posiciones del queso y la rata
        self.tamano()
        self.setPosicionRata(0, 0)
        self.setPosicionQueso(self.shape[0] - 1, self.shape[1] - 1)
        self.resetear()

    def tamano(self):
        """Metodo que devuelve una tupla con la cantidad de filas y columnas"""
        self.shape = self.laberinto.shape[:-1]

    def resetear(self):
        """metodo que limpia el laberinto"""
        self.res_lab = []
        for i in range(self.shape[0]):
            fila = []
            for j in range(self.shape[1]):
                fila.append([False, False])
            self.res_lab.append(fila)

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
        for elem in self.laberinto[i, j, :]:
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
        return {'visitada': self.res_lab[i][j][0], 'caminoActual': self.res_lab[i][j][1]}

    def resuelto(self):
        """devuelve True si el laberinto está resuelto, es decir, si la posición de la rata es la misma que
        la del queso, y False en otro caso"""
        return self.PosQueso == self.PosRata

    def resolver(self):


        if self.resuelto():
            return True
        else:

            i = self.PosRata[0]
            j = self.PosRata[1]

            # obtiene los lugares del laberinto hacia donde es posible moverse
            paredes = self.get(i, j)


            if (not paredes[0]) and (not self.getInfoCelda(i-1, j).get('visitada')):
                self.setPosicionRata(i-1, j)
                self.res_lab[i, j, 1] = 1
            elif (not paredes[1]) and (not self.getInfoCelda(i, j-1).get('visitada')):
                self.setPosicionRata(i, j-1)
                self.res_lab[i, j, 1] = 1
            elif (not paredes[2]) and (not self.getInfoCelda(i + 1, j).get('visitada')):
                self.setPosicionRata(i + 1, j)
                self.res_lab[i, j, 1] = 1
            elif (not paredes[3]) and (not self.getInfoCelda(i, j + 1).get('visitada')):
                self.setPosicionRata(i, j + 1)
                self.res_lab[i, j, 1] = 1


            elif paredes[1]:
            # me fijo hacia donde me puedo mover, en funcion de si ya fue visitada la casilla
            if not paredes[1]:


            self._volver()
            self.resolver()


    # COMPLETAR CON LOS METODOS PEDIDOS

    # auxiliares (metodos privados)

    def _redibujar(self):
        if self.parent is not None:
            self.parent.update()