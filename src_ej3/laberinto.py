# -*- coding: utf-8 -*-
import ast


class Laberinto(object):
    """"Vamos de definir funciones para crear un laberinto.
    La función init se inicializa siempre que se llama a la clase Laberinto """

    def __init__(self, parent=None):
        self.parent = parent

    # interfaz (metodos publicos)

    def cargar(self, fn):
        """Carga un archivo .txt que representa al laberinto"""

        self.fn = fn
        with open(fn, "r") as entrada:
            return entrada

    def cargar1(self, fn):
        """"Carga un laberinto a partir de un archivo .lab"""

        with open(fn, 'r') as entrada:
            laberinto = []      # laberinto a llenar
            corch1 = '['        # creo unas cadenas para poder rellenar el ppio y el final de los split
            corch2 = ']'
            next(entrada)       # saltea la primera linea
            for linea in entrada:       # recorre la entrada (desde la segunda linea)
                linea = linea.strip('\n').lstrip('[').rstrip(']')       # recorte del \n y del corchete inicial y final
                fila = []               # vacia la fila para cada itereacion
                for casillero in linea.split(']['):     # divide la linea donde abren y cierran corchetes
                    fila.append(ast.literal_eval(corch1+casillero+corch2))   # ast.lit pasa un str a lista
                laberinto.append(fila)  # agrego la fila al laberinto
        return laberinto

    def tamano(self):
        """Devuelve una tupla con la cantidad de filas y columnas"""

    def resetear(self):
        """limpia el laberinto"""

    def getPosicionRata(self):
        """devuelve una tupla con las coordenadas de la rata"""

    # COMPLETAR CON LOS METODOS PEDIDOS

    # auxiliares (metodos privados)

    def _redibujar(self):
        if self.parent is not None:
            self.parent.update()
