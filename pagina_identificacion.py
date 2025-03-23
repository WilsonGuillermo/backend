""" Pagina de identificacion """
""" Version 3, 09-04 a 11h """
""" nombre unico del fichero """
""" Agregamos el cadre de la pagina principal """

# coding: utf-8

import tkinter as tk
import random as rd
import gestion_bdd as mibase
#import gestion_cocina as micocina
#import gestion_admin as admin


# CONSTANTES

class identificacion(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        #super().__init__()
        tk.Tk.__init__(self)       # contructor de la clase madre

        # Somos una instancia de la cocina
        self.bdd = mibase.mi_base()
        #self.micocina = micocina.cocina()

        self.title("Pintando Ando")
        self.geometry("720x520")
        self.minsize(420,300)
        #self.admin = admin.admin()

        #self.grid()

        self.crear_componentes_identificacion()

    def crear_componentes_identificacion(self):
        """ Crear y posicionar botones """

        self.frame = tk.Frame( self.master, bg='#41B77F', bd=1, relief='sunken')

        # Crear y posicionar los widgets
        self.label0 = tk.Label( self.frame, text = 'Bienvenido - Pagina de Identificacion', font=('courrier', 25))
        self.label0.pack(pady=20)

        self.label1 = tk.Label( self.frame, text = 'Por favor escribe tu usuario: ', font=('courrier', 15))
        self.label1.pack(pady=20)

        self.display1 = tk.Entry( self.frame, font=("Arial", 24), bg='darkblue', fg='red', borderwidth=0) # Falta borrar lo escrito
        self.display1.pack(pady=20)

        self.label2 = tk.Label( self.frame, text = 'Por favor escribe tu clave: ', font=('courrier', 15)) 
        self.label2.pack(pady=20)

        self.display2 = tk.Entry( self.frame, font=("Arial", 24), bg='darkred', fg='red', borderwidth=0) # Falta borrar lo escrito
        self.display2.pack(pady=20)
        
        self.boton_busqueda = tk.Button( self.frame, text = 'Valider', command = self.celula_de_identificacion)
        self.boton_busqueda.pack(pady=20)

        # Boton para salir de la aplicacion
        self.bouton_salir = tk.Button( self.frame, text = "Salir", command = self.quit )
        self.bouton_salir.pack(side=tk.BOTTOM, pady=20)

        self.frame.pack()

    def celula_de_identificacion(self):
        """ recuperamos el valor escrito y lo enviamos a la funcion """

        #usuario = "Felipe"

        #contrasena  = "WilsonMemo1"

        usuario = self.display1.get()

        contrasena  = self.display2.get()

        print("el valor a enviar ahora mismo es: ",usuario," y ", contrasena)

        requete = "select * from usuarios where nombre_usuario = '%s' and contrasena = '%s'"%(usuario,contrasena)
        
        print("******************************************")

        print("enviamos: ", requete)

        print("******************************************")

        papel = self.bdd.consultacion_usuario(requete)

        return papel
    
if __name__ == "__main__":
    app = identificacion()
    app.title("Boutique, gestion de los productos de la cocina")
    app.mainloop()   