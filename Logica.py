# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:45:07 2020
@author: Alguien, JSM1 y JSM2
"""

class Temporalizador:
    def __init__(self):
        '''inicializa el Temporalizador con 0 segundos y pausado'''
        self.tReal = 0
        self.tAct = 0
        self.breaker = False

    def setTReal(self, t: int):
        self.tReal = t

    def setTAct(self, t: int):
        self.tAct = t

    def setBreak(self, b: bool):
        self.breaker = b

    def getTReal(self) -> int:
        return self.tReal

    def getTAct(self) -> int:
        return self.tAct

    def getBreak(self) -> bool:
        return self.breaker

    def reset(self):
        self.ingresarT(self.tReal)

    def ingresarT(self,t: int):
        self.setTReal(t)
        self.setTAct(t)

    def iniciarCont(self, t: int):
        self.ingresarT(t)
        self.setBreak(True)

    def contar(self):
        self.setTAct(self.getTAct()-1)
        '''for i in range(1,tiempo+1):
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
                x='ok' '''

def main():
    rut = Temporalizador()
    rut.iniciarCont(30)
    while rut.getTAct()>0 and rut.getBreak() == True:
        print(rut.getTAct())
        rut.contar()
