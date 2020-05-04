# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:45:07 2020

@author: (╯°□°)╯︵ ┻━┻
"""



import time
class Logica:
    def __init__(self):
        self.tiempoT=0

    def igresoTTotal(self,tiempoT):
        self.tiempoT=tiempoT
        
    def diviMin(self,muni):
        pass
    def cornometro(self):
        pass 
        
        

def contar(h,m,s):
       horas=0
       segun=0
       minu=0
       #horas<=h and segun<=s or minu<=m 
       x='q'
       while (x !='ok'):
           segun=segun+1           
           if(segun==60):
               segun=0
               minu=minu+1
           if(minu==60):    
               minu=0
               horas=horas+1
           print(str(horas)+':'+str(minu)+':'+str(segun))
           if(horas==h and minu==m and segun==s):
               x='ok'
           time.sleep(1)
horas=input('ingrese hora')
minutos=input('ingrese minutos')
segundos=input('ingrese segundos')
limite=contar(int(horas),int(minutos),int(segundos))