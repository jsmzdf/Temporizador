# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:45:07 2020

@author: (╯°□°)╯︵ ┻━┻
"""



import time
class Temporizador:
    def __init__(self):
        self.tiempoT=0

    def ingresoTTotal(self,tiempoT):
        self.tiempoT=tiempoT
        
    def mostrar(self,i,segu,mesaje):
        
        return i,segu,mesaje
    
        
    def contar(tiempo,ejercicio):
        
        for i in range(1,tiempo+1):
          tiempooras=i
          segun=0
          minu=0
          x='q'
          mesaje="ejecicio"
          while (x !='ok'):
            segun=segun+1 
            minu=minu+1          
            if(segun==60):
                segun=0
                
            print(minu)
            print(str(i)+':'+str(segun))
            
            if(segun==ejercicio):
               mesaje="descanso"      
                
            if(minu==60):
                x='ok'
            time.sleep(1)
    
horas=input('ingrese tiempo total')

ejercicio=input('ingrese segundos')
Temporizador.contar(int(horas),int(ejercicio))