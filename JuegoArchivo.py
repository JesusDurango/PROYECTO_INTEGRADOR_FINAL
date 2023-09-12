import  os, random
from Juego import *
class JuegoArchivo(Juego):
    def __init__ (self,archivo):
        self.archivo = f"{archivo}/{random.choice(os.listdir(archivo))}" 
        mapa, pos_ini, pos_fin = self.leer()
        Juego.__init__(self,mapa , pos_ini, pos_fin)
        
        
        
    def leer(self):
        
        with open(self.archivo,"r")as leerArchivo:
            lineas = leerArchivo.readlines()
            posiciones = list(map(int,lineas[0].strip().split()))
            mapa = list(map(lambda linea : list (linea.strip()), lineas[1:]))
            return mapa, posiciones[:2],posiciones[2:]
    

juego1 = JuegoArchivo("maps")
juego1.main_loop()
