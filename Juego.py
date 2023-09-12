from os import system,name 
from readchar import key,readkey 

class Juego:
    def __init__(self,mapa,posicion_inicial,posicion_final):
    
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        

    def update_screen(self):
        system('cls' if name == 'nt' else 'clear')
        for row in self.mapa:
            print(''.join(row))
        
        
    def main_loop(self):
        py, px = self.posicion_inicial
        
        
        while (list((py,px)) != self.posicion_final): 
            self.mapa[py][px]= 'P'
            self.update_screen()
            
            while True:
                
                character =  readkey()
                if character == key.UP:
                    if (py-1) in range (0, len(self.mapa)):
                        if self.mapa[py-1][px] == '.':
                            self.mapa[py][px] = '.'
                            py -= 1
                            self.mapa[py][px] = 'P'
                            break
                if character == key.DOWN:
                    if (py+1) in range (0, len(self.mapa)):
                        if self.mapa[py+1][px] == '.':
                            self.mapa[py][px] = '.'
                            py += 1
                            self.mapa[py][px] = 'P'
                            break
                if character == key.LEFT:
                    if (px-1) in range (0, len(self.mapa[0])):
                        if self.mapa[py][px-1] == '.':
                            self.mapa[py][px]= '.'
                            px -= 1
                            self.mapa[py][px] = 'P'
                            break
                if character == key.RIGHT:
                    if px+1 in range (0, len( self.mapa[0])):
                        if self.mapa[py][px+1] == '.':
                            self.mapa[py][px] = '.'
                            px += 1
                            self.mapa[py][px] ='P'
                            break
    
    