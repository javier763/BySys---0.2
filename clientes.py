from tkinter import *
import tkinter as tk
from tkinter import ttk


class Clientes (tk.Frame):
    
    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()


#///////////////////////////Nombre//////////////////////////
    def widgets(self):
        self.labelframe = tk.LabelFrame(self, text="Clientes", font="sans 20 bold", bg="#C6D9E3")
        self.labelframe.place(x=20, y=20, width=250, height=560)

        lblnombre = tk.Label(self.labelframe, text="Nombre:", font="sans 14 ", bg="#C6D9E3")
        lblnombre.place(x=10, y=20)

        self.nombre = ttk.Entry(self.labelframe, font="sans 14")
        self.nombre.place(x=10, y=50, width=220, height=40)
        
        lblnombre = tk.Label(self.labelframe, text="Apellidos:", font="sans 14", bg="#C6D9E3")
        lblnombre.place(x=10, y=120)
        
        self.nombre = ttk.Entry(self.labelframe, font="sans 14")
        self.nombre.place(x=10, y=150, width=220, height=40)
        
        lblnombre = tk.Label(self.labelframe, text="Correo del cliente:", font="sans 14", bg="#C6D9E3")
        lblnombre.place(x=10, y=210)
        
        self.nombre = ttk.Entry(self.labelframe, font="sans 14")
        self.nombre.place(x=10, y=240, width=220, height=40)
        
#///////////////////////FIN/////////////////////////


 