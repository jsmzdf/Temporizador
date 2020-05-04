# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:49:04 2020

@author: Alguien, JSM1 y JSM2
"""


import tkinter as tk
from tkinter import messagebox
from Logica import *
from winsound import *

rut = Temporalizador()

def Conteo():
    if rut.getBreak() == True:
        if rut.getTAct() > 0:
            marco.after(1000,lambda:[rut.contar(),tRut.set(str(float(tTot.get()) - float(tInt.get()) + float(float(rut.getTAct()) / 60.0))), Conteo()])
        else:
            if float(tRut.get()) > 0:
                PlaySound("alarm.wav", SND_FILENAME)
                Run()
            else:
                Rest()
prueba=True

def Run():
    global prueba
    
    if(prueba==True):
        print(prueba)
        try:
            iRut = float(tRut.get())
            iInt = float(tInt.get())
        except:
            messagebox.showerror(title="Error", message="Ingrese solo numeros, porfavor")
            tRut.set(0)
            tInt.set(0)
            return
        nInt.set(int(iRut/iInt))
        tRut.set(str(float(int(nInt.get())*float(tInt.get()))))
        tTot.set(float(iRut))
        rut.iniciarCont(iInt*60)
        Conteo()
        '''for n in range(nInt):
            rut.iniciarCont(iInt*60+1)
            tRut.set(str(float(int(nInt-n)*float(tInt.get()))-int(iInt*60)+rut.getTAct()))
            print(str(float(int(nInt-n)*float(tInt.get()))-int(iInt*60)+rut.getTAct()))
            rut.contar()'''
        prueba=False        
    
def Stop():
    if rut.getBreak() == True:
        rut.setBreak(False)
    else:
        rut.setBreak(True)
    Conteo()


def Rest():
    global prueba
    prueba=True
    tRut.set(str(float(int(nInt.get())*float(tInt.get()))))

marco = tk.Tk()
nInt = tk.StringVar()
tTot = tk.StringVar()
marco.title('Contador con rutina')
tk.Label(marco,bg="#202020",fg="white").grid(row=0, column=0, columnspan=4)
tk.Label(marco, text="Tiempo de la rutina: ",bg="#202020",fg="white").grid(row=1, column=0, columnspan=3)
tRut = tk.StringVar()
tRut.set('10')
txRut = tk.Entry(marco, textvariable=tRut)
txRut.grid(row=1, column=3)
tk.Label(marco, text=" min",bg="#202020",fg="white").grid(row=1, column=4)
tk.Label(marco, text="Tiempo por intervalos: ",bg="#202020",fg="white").grid(row=2, column=0, columnspan=3)
tInt = tk.StringVar()
tInt.set('0.5')
txInt = tk.Entry(marco, textvariable=tInt)
txInt.grid(row=2, column=3)
tk.Label(marco, text=" min",bg="#202020",fg="white").grid(row=2, column=4)
btn=tk.Button(marco, text='Empezar', command=Run).grid(row=3, column=0)
btn=tk.Button(marco, text='Detener/Continuar', command=Stop).grid(row=3, column=1)
btn=tk.Button(marco, text='Reiniciar', command=Rest).grid(row=3, column=2)

def main():
    marco.configure(background='#202020')
    marco.geometry('450x200')
    marco.mainloop()
    pass

if __name__ == '__main__':
    main()
