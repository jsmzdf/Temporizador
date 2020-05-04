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

      segun=0
      minu=0
      x='q'
      mesaje="ejecicio"
      while (x !='ok'):
        segun=segun+1 
        minu=minu+1          
        if(segun==60):
            segun=0   
        
        if(segun==ejercicio):
           mesaje="descanso"      
            
        if(minu==60):
            x='ok'
        time.sleep(1)

def contarMin(tiempo,ejercicio):
    segun=0
    minu=0
    mesaje="ejecicio"
    segun=segun+1 
    minu=minu+1          
    if(segun==60):
        segun=0   
    if(segun==ejercicio):
       mesaje="descanso"          
    if(minu==60):
        return contarMin(tiempo,ejercicio)
    time.sleep(1)
    
    
    
    
def contar(segun,tiempo,ejercicio):
    time.sleep(1)
    print(segun)
    if(segun<=ejercicio):
       mesaje="ejer4cicio"
       print(mesaje)
       return mesaje,segun,contar(segun+1,tiempo,ejercicio)
    if(segun >ejercicio and segun<60):
        mesaje="descanso"
        print(mesaje)
        return mesaje,segun,contar(segun+1,tiempo,ejercicio)
    
    
def contar1(tiempooras,tiempo,ejercicio):
    print(tiempooras,tiempo,ejercicio)
    if(tiempo > tiempooras):
        return [tiempooras+1,contar(1,tiempo,ejercicio),contar1(tiempooras+1,tiempo,ejercicio)]
    else:
        return ["complete"]
    
horas=input('ingrese tiempo total')

ejercicio=input('ingrese segundos')
#Temporizador.contar(int(horas),int(ejercicio))
print("segu")
#print(contar(1,int(horas),int(ejercicio)))
print("ejercicio")
print(contar1(0,int(horas),int(ejercicio)))
