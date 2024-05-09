""" afichage de la pagina control
    de Platos del dia """
""" Version 1 """

# coding: utf-8

import tkinter as tk
import random as rd
#import cocina_plus_bdd_7 as cocina
import gestion_bdd as mibase

# CONSTANTES
DESCONOCIDO = "producto desconocido"

ser_o_estar = None

class Gestion_Platos_Del_Dia(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        tk.Tk.__init__(self)       # contructor de la clase madre

        self.crear_componentes()

    def crear_componentes(self):
        pass

if __name__ == "__main__":
    app = Gestion_Platos_Del_Dia()
    app.title("Boutique, gestion de los platos del dia")
    app.mainloop()