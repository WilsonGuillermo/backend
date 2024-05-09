""" Pagina de Gestion de ingredientes """
""" Version 1, 09-04 a 11h """
""" nombre unico del fichero """

# coding: utf-8

import tkinter as tk
import gestion_bdd as mibase
import gestion_cocina as micocina
#import gestion_admin as admin

# CONSTANTES

class Ingredientes(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        #super().__init__()
        tk.Tk.__init__(self)       # contructor de la clase madre

        # Somos una instancia de la cocina
        self.bdd = mibase.mi_base()

        #self.title("Pintando Ando - Gestion de productos")
        #self.geometry("720x520")
        #self.minsize(420,300)
        #self.admin = admin.admin()

        #self.grid()

        self.crear_componentes_ingredientes()

    def crear_componentes_ingredientes(self):
        """ Crear y posicionar botones """

        self.frame = tk.Frame( self.master, bg='#41B77F', bd=1, relief='sunken')

        # Crear y posicionar los widgets
        self.label1 = tk.Label( self.frame, text = 'Bienvenido - Pagina de gestion de Ingredientes', font=('courrier', 25))
        self.label1.pack(pady=20)

        self.label2 = tk.Label( self.frame, text = 'Selecciona el ingredientes por favor', font=('courrier', 15))
        self.label2.pack(pady=20)

        self.listbox = tk.Listbox( self.frame, font=('courrier', 25))
        
        interrogation = "select nombre from referencia_ingredientes"
        resultados = self.bdd.consultacion_generique(interrogation) 
        i=1
        for fila in resultados:
            self.listbox.insert(i, fila)
            i = i + 1
        self.listbox.pack(pady=10)

        self.label_mas = tk.Label( self.frame, text = 'Aumentar el stock de ')
        self.label_mas.pack(pady=20)

        self.campo1 = tk.Entry( self.frame, font=("Arial", 24), bg='darkred', fg='red', borderwidth=0) # Falta borrar lo escrito
        self.campo1.pack()

        #self.boton_mas = tk.Button( self.frame, text = 'Validar', command = self.aumentar_stock)
        self.boton_mas = tk.Button( self.frame, text = 'Validar')
        self.boton_mas.pack(pady=20)

        self.label_menos = tk.Label( self.frame, text = 'Disminuir el stock de ')
        self.label_menos.pack(pady=20)

        self.campo2 = tk.Entry( self.frame, font=("Arial", 24), bg='darkred', fg='red', borderwidth=0) # Falta borrar lo escrito
        self.campo2.pack()

        #self.boton_menos = tk.Button( self.frame, text = 'Validar', command = self.disminuir_stock)
        self.boton_menos = tk.Button( self.frame, text = 'Validar')
        self.boton_menos.pack(pady=20)

        #self.boton_verificacion = tk.Button( self.frame, text = 'Desea recuperar el stock del producto?', command = self.verificar_stock)
        self.boton_verificacion = tk.Button( self.frame, text = 'Desea recuperar el stock del producto?')
        self.boton_verificacion.pack(pady=20)

        # Boton para salir de la aplicacion
        #self.bouton_volver = tk.Button( self.frame, text = "Volver al menu", command = self.volver )
        self.bouton_volver = tk.Button( self.frame, text = "Volver al menu" )
        self.bouton_volver.pack(side=tk.BOTTOM, pady=20)

        # Boton para salir de la aplicacion
        #self.bouton_salir = tk.Button( self.frame, text = "Salir", command = self.quit )
        self.bouton_salir = tk.Button( self.frame, text = "Salir" )
        self.bouton_salir.pack(side=tk.BOTTOM, pady=20)

        self.frame.pack()

if __name__ == "__main__":
    app = Ingredientes()
    app.title("Boutique, gestion de los productos de la cocina")
    app.mainloop()   