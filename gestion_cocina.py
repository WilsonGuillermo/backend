""" Pagina de Gestion de la cocina """
""" Version 2 """
""" Agregamos todas las actividades """

# coding: utf-8

import tkinter as tk
import random as rd
import gestion_bdd as mibase
#import gestion_admin as admin
import pagina_gestion_ingredientes as ingredientes
import pagina_cocina_menus as menus
import pagina_cocina_p_del_dia as platos_del_dia
import pagina_cocina_p_informales as platos_informales
import pagina_cocina_bebidas as bebidas
import pagina_cocina_postres as postres

# CONSTANTES

class cocina(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        tk.Tk.__init__(self)       # contructor de la clase madre

        # Somos una instancia de la cocina
        self.bdd = mibase.mi_base()
        #self.admin = admin.admin()
        self.ingredientes =  ingredientes.Ingredientes()
        self.menus = menus.Gestion_Menus()
        self.platos_del_dia = platos_del_dia.Gestion_Platos_Del_Dia()
        self.platos_informales = platos_informales.Gestion_Platos_Informales()
        self.bebidas = bebidas.Gestion_Bebidas()
        self.postres = postres.Gestion_Postres()

        #self.grid()

        self.crear_componentes_cocina()

    def crear_componentes_cocina(self):
        """ Crear y posicionar botones """

        print("estoy aqui, aqui...")
        self.frame = tk.Frame( self.master, bg='#41B77F', bd=1, relief='sunken')
        # Crear y posicionar los widgets
        self.label = tk.Label( self, text = 'Bienvenido a la Boutique - Pagina para gestionar la cocina')
        self.label.pack(pady=20)

        self.label1 = tk.Label( self, text = 'Que deseas hacer ?')
        self.label1.pack(side='left', pady=20)

        self.boton_producto = tk.Button( self, text = 'Modificar la cantidad de stockage de un producto', command = self.ingredientes.crear_componentes_ingredientes )
        self.boton_producto.pack(pady=20)

        self.boton_menu = tk.Button( self, text = 'Modificar los menus, command = self.menus')
        self.boton_menu.pack(pady=20)

        self.boton_p_dia = tk.Button( self, text = 'Modificar los platos del dia, command = self.platos_del_dia')
        self.boton_p_dia.pack(pady=20)

        self.boton_p_informales = tk.Button( self, text = 'Modificar los platos informales, command = self.platos_informales')
        self.boton_p_informales.pack(pady=20)

        self.boton_bebidas = tk.Button( self, text = 'Modificar las bebidas, command = self.bebidas')
        self.boton_bebidas.pack(pady=20)

        self.boton_postres = tk.Button( self, text = 'Modificar los postres, command = self.postres')
        self.boton_postres.pack(pady=20)

        # Boton para salir de la aplicacion
        self.bouton_salir = tk.Button( self, text = "Salir", command = self.quit )
        self.bouton_salir.pack(side=tk.BOTTOM, pady=20)

if __name__ == "__main__":
    app = cocina()
    app.title("Boutique, gestion del chef de cocina")
    app.mainloop()