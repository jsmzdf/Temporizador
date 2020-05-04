# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:49:04 2020

@author: Alguien, JSM1 y JSM2
"""


import tkinter as tk
from tkinter import messagebox
from Logica import *

rut = Temporalizador()

def Conteo():
    if rut.getBreak() == True:
        marco.after(1000,lambda:[rut.contar(), print(rut.getTAct()),tRut.set(str(rut.getTAct())), Conteo()])

def Run():
    try:
        iRut = float(tRut.get())
        iInt = float(tInt.get())
    except:
        messagebox.showerror(title="Error", message="Ingrese solo numeros, porfavor")
        tRut.set(0)
        tInt.set(0)
        return
    nInt = int(iRut/iInt)
    rut.iniciarCont(iInt*60)
    Conteo()
    '''for n in range(nInt):
        rut.iniciarCont(iInt*60+1)
        tRut.set(str(float(int(nInt-n)*float(tInt.get()))-int(iInt*60)+rut.getTAct()))
        print(str(float(int(nInt-n)*float(tInt.get()))-int(iInt*60)+rut.getTAct()))
        rut.contar()'''

def Stop():
    if rut.getBreak() == True:
        rut.setBreak(False)

def Rest():
    pass

def Bipoff():
    pass

marco = tk.Tk()
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
btn=tk.Button(marco, text='Detener', command=Stop).grid(row=3, column=1)
btn=tk.Button(marco, text='Reiniciar', command=Rest).grid(row=3, column=2)
btn=tk.Button(marco, text='Detener Alarma', command=Bipoff).grid(row=3, column=3)

def main():
    marco.configure(background='#202020')
    marco.geometry('350x200')
    marco.mainloop()
    pass

if __name__ == '__main__':
    main()
