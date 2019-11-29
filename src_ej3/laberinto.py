# -*- coding: utf-8 -*-

class Laberinto(object):
    """Vamos de definir funciones para crear un laberinto """
	
    #La función init se inicializa siempre que se llama a la clase Laberinto
    def __init__(self, parent=None):
        self.parent = parent
   
	##### interfaz (metodos publicos)
    def cargar(self,fn):
        "Carga un archivo .txt que representa al laberinto"
        self.fn = fn
        with open (fn,"r") as entrada:
            return entrada
    
    def tamano(self):
        "Devuelve una tupla con la cantidad de filas y columnas"
    
    def resetear(self):
        "limpia el laberinto"
    
    def getPosicionRata(self):
        "devuelve una tupla con las coordenadas de la rata"
        
    
    
	####
	#### COMPLETAR CON LOS METODOS PEDIDOS
	####

	##### auxiliares (metodos privados)

"""
	def _redibujar(self):
	    if self.parent is not None:
	        self.parent.update()
"""