import tkinter as tk
import tkinter.messagebox as telegrama
#import pagina_identificacion as buscando_profil
import gestion_bdd as mibase

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("720x480")
        self.title("Aplicación Boutique")
        self.config(background = '#4065A4')
        
        self.frame_identificacion = IdentificacionFrame(self)
        self.frame_identificacion.pack(fill="both", expand=True)
        
        self.frame_perfiles_admin = PerfilesFrameAdmin(self)
        self.frame_perfiles_cocinero = PerfilesFrameCocinero(self)
        self.frame_perfiles_mesero = PerfilesFrameMesero(self)
        self.frame_perfiles_jardinero = PerfilesFrameJardinero(self)
        self.frame_perfiles_responsable = PerfilesFrameResponsable(self)
        
        # Ocultar los otros frames al inicio
        self.frame_perfiles_admin.pack_forget()
        self.frame_perfiles_cocinero.pack_forget()
        self.frame_perfiles_mesero.pack_forget()
        self.frame_perfiles_jardinero.pack_forget()
        self.frame_perfiles_responsable.pack_forget()

        # Evento para identificar al usuario y mostrar el perfil correspondiente
        self.frame_identificacion.boton_identificar.config(command=self.identificar_usuario)

    def identificar_usuario(self):
        # Aquí deberías implementar la lógica para identificar al usuario
        # y obtener su perfil

        usuario = self.frame_identificacion.display1.get()

        contrasena  = self.frame_identificacion.display2.get()

        print("el valor a enviar ahora mismo es: ",usuario," y ", contrasena)

        requete = "select * from usuarios where nombre_usuario = '%s' and contrasena = '%s'"%(usuario,contrasena)
        
        print("******************************************")

        self.base = mibase.mi_base()
        
        papel = self.base.consultacion_usuario(requete)
        
        print("le profil es: ",papel)

        ######################
        
        #  Verificamos si el usuario existe
        if papel == 'Admin':
            """ Administrador """
            self.frame_perfiles_admin.pack(fill="both", expand=True)
        elif papel == 'Cocinero':
            """ Concinero """
            self.frame_perfiles_cocinero.pack(fill="both", expand=True)
        elif papel == 'Mesero':
            """ Mesero """
            self.frame_perfiles_mesero.pack(fill="both", expand=True)
        elif papel == 'Jardinero':
            """ Jardinero """
            self.frame_perfiles_jardinero.pack(fill="both", expand=True)
        elif papel == 'Responsable':
            """ Responsable """
            self.frame_perfiles_responsable.pack(fill="both", expand=True)
        else:
            """ El profil no existe """
            telegrama.showinfo("Error", message = f"La pareja 'identificador:contrasena' no existe, intentalo de nuevo")
            # Limpiar los campos de entrada 'login/mdp'
            print("1")
            self.frame_identificacion.display1.delete(0,tk.END)
            print("2")
            self.frame_identificacion.display2.delete(0,tk.END)
            print("3")
            #self.frame_perfiles_responsable.pack_forget()
            print("4")
            #self.identificar_usuario()
            #self.frame_identificacion.pack()
            print("5")
            self.frame_identificacion.destroy()
            self.frame_perfiles_cocinero.destroy()
            self.frame_perfiles_admin.destroy()
            self.frame_perfiles_mesero.destroy()
            self.frame_perfiles_jardinero.destroy()
            self.frame_perfiles_responsable.destroy()
            print("6")
            Aplicacion()
            #self.frame_identificacion = IdentificacionFrame(self)
            print("7")
            #self.frame_identificacion.pack()
            print("8")
            
            #self.frame_identificacion.boton_identificar.config(command=self.identificar_usuario)
        #########################



        # Mostrar el frame correspondiente al perfil del usuario y esconder el principal
        self.frame_identificacion.pack_forget()

class IdentificacionFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        #self.frame.config(bg='#41B77F', bd=1, relief='sunken')
        #self.label_identificacion = tk.Label(self, text="Identificación de usuario")
        #self.label_identificacion.pack()

        ##########
        # Crear y posicionar los widgets
        self.label0 = tk.Label( self, text = 'Bienvenido - Pagina de Identificacion', font=('courrier', 25))
        self.label0.pack(pady=20)

        self.label1 = tk.Label( self, text = 'Por favor escribe tu usuario: ', font=('courrier', 15))
        self.label1.pack(pady=10)

        self.display1 = tk.Entry( self, font=("Arial", 24), bg='darkblue', fg='red', borderwidth=0) # Falta borrar lo escrito
        self.display1.pack(pady=10)

        self.label2 = tk.Label( self, text = 'Por favor escribe tu clave: ', font=('courrier', 15)) 
        self.label2.pack(pady=10)

        self.display2 = tk.Entry( self, font=("Arial", 24), bg='darkred', fg='red', borderwidth=0, show = "*") # Falta borrar lo escrito
        self.display2.pack(pady=10)
        
        self.boton_identificar = tk.Button(self, text="Identificar")
        self.boton_identificar.pack(pady=10)

        # Boton para salir de la aplicacion
        self.bouton_salir = tk.Button( self, text = "Salir", command = self.quit )
        self.bouton_salir.pack(side=tk.BOTTOM, pady=20)

class PerfilesFrameAdmin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label_perfiles = tk.Label(self, text="Perfil admin")
        self.label_perfiles.pack()

        # Aquí podrías agregar más widgets específicos para cada perfil

class PerfilesFrameMesero(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label_perfiles = tk.Label(self, text="Perfil mesero")
        self.label_perfiles.pack()

        # Aquí podrías agregar más widgets específicos para cada perfil

class PerfilesFrameJardinero(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label_perfiles = tk.Label(self, text="Perfil jardinero")
        self.label_perfiles.pack()

        # Aquí podrías agregar más widgets específicos para cada perfil

class PerfilesFrameResponsable(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label_perfiles = tk.Label(self, text="Perfil responsable")
        self.label_perfiles.pack()

        # Aquí podrías agregar más widgets específicos para cada perfil

class PerfilesFrameCocinero(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.framecocinero = tk.Frame(self, relief='solid' )

        self.label_perfiles = tk.Label( self.framecocinero, text = 'Pagina de Gestion del Sr. Cocinero', font=('courrier', 25))
        self.label_perfiles.pack(pady=20)

        self.frame_gestion_cocina = GestionCocinaFrame(self)
        self.frame_gestion_inventario = GestionInventarioFrame(self)
        
        # Ocultar los otros frames al inicio
        self.frame_gestion_cocina.pack_forget()
        self.frame_gestion_inventario.pack_forget()

        # Mostrar los frames correspondientes a las opciones del perfil
        self.boton_gestion_cocina = tk.Button(self.framecocinero, text="Gestión de Cocina", command=self.mostrar_gestion_cocina)
        self.boton_gestion_cocina.pack(pady=10)

        self.boton_gestion_inventario = tk.Button(self.framecocinero, text="Gestión de Inventario", command=self.mostrar_gestion_inventario)
        self.boton_gestion_inventario.pack(pady=10)

        self.framecocinero.pack()

    def mostrar_gestion_cocina(self):
        self.frame_gestion_cocina.pack(fill="both", expand=True)
        self.frame_gestion_inventario.pack_forget()
        self.framecocinero.pack_forget()

    def mostrar_gestion_inventario(self):
        self.frame_gestion_inventario.pack(fill="both", expand=True)
        self.frame_gestion_cocina.pack_forget()
        self.framecocinero.pack_forget()

class GestionCocinaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        """ Vamos a gestionar el stock de un producto """
            
        """ Afichar el menu de opciones del producto """
        self.framemenu = tk.Frame(self, relief='groove', bg='#41B77F', bd=1)

        self.frame_producto = GestionProductoFrame(self)
        self.frame_menu = GestionMenuFrame(self)
        self.frame_plato_del_dia = GestionPlatoDiaFrame(self) # a completar las otras opciones
        
        # Ocultar los otros frames al inicio
        self.frame_producto.pack_forget()
        self.frame_menu.pack_forget()
        self.frame_plato_del_dia.pack_forget() # a completar las otras opciones

        self.label = tk.Label( self.framemenu, text = 'Pagina para gestionar la cocina', font = ('courrier', 25), background = '#41B77F')
        self.label.pack(pady=20)

        self.label1 = tk.Label( self.framemenu, text = 'Que deseas hacer ?', background = '#41B77F')
        self.label1.pack(side='top', pady=5)

        self.framebotones = tk.Frame(self.framemenu, bg='#4065A4', bd=1, relief='sunken')

        self.boton_producto = tk.Button( self.framebotones, text = 'Modificar la cantidad de stockage de un producto', command = self.producto )
        self.boton_producto.pack(pady=5)

        self.boton_menu = tk.Button( self.framebotones, text = 'Modificar los menus')
        #self.boton_menu = tk.Button( self.framebotones, text = 'Modificar los menus', command = self.menus)
        self.boton_menu.pack(pady=5)

        self.boton_p_dia = tk.Button( self.framebotones, text = 'Modificar los platos del dia')
        #self.boton_p_dia = tk.Button( self.framebotones, text = 'Modificar los platos del dia', command = self.platos_del_dia)
        self.boton_p_dia.pack(pady=5)

        self.boton_p_informales = tk.Button( self.framebotones, text = 'Modificar los platos informales')
        #self.boton_p_informales = tk.Button( self.framebotones, text = 'Modificar los platos informales', command = self.platos_informales)
        self.boton_p_informales.pack(pady=5)

        self.boton_bebidas = tk.Button( self.framebotones, text = 'Modificar las bebidas')
        #self.boton_bebidas = tk.Button( self.framebotones, text = 'Modificar las bebidas', command = self.bebidas)
        self.boton_bebidas.pack(pady=5)

        self.boton_postres = tk.Button( self.framebotones, text = 'Modificar los postres')
        #self.boton_postres = tk.Button( self.framebotones, text = 'Modificar los postres', command = self.postres)
        self.boton_postres.pack(pady=5)

        # Boton para salir de la aplicacion
        self.bouton_salir = tk.Button( self.framemenu, text = "Salir", command = self.quit )
        self.bouton_salir.pack(side=tk.BOTTOM, pady=20)

        self.framebotones.pack()

        self.framemenu.pack()

    def producto(self):
        """ Vamos a modificar la cantidad de un producto"""
        self.frame_producto.pack()
        self.frame_menu.pack_forget()
        self.frame_plato_del_dia.pack_forget()
        self.framebotones.pack_forget()
        self.framemenu.pack_forget()


class GestionProductoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.base = mibase.mi_base()

        # Aquí puedes agregar widgets para la gestión del inventario
        self.frame = tk.Frame( self, bg='#41B77F', bd=1, relief='sunken')

        # Crear y posicionar los widgets
        self.label1 = tk.Label( self.frame, text = 'Pagina de gestion de Ingredientes', font=('courrier', 25))
        self.label1.pack(pady=20)

        self.framelista = tk.Frame( self.frame, bg='#41B77F', bd=1, relief='sunken')

        self.label2 = tk.Label( self.framelista, text = 'De la lista, selecciona el ingredientes por favor', bg='#41B77F', font=('courrier', 10))
        self.label2.pack(pady=5)

        self.listbox = tk.Listbox( self.framelista, font=('courrier', 10), bg='#41B77F')
        
        interrogation = "select nombre from referencia_ingredientes"
        resultados = self.base.consultacion_generique(interrogation) 
        i=1
        for fila in resultados:
            self.listbox.insert(i, fila)
            i = i + 1
        
        self.listbox.pack(pady=10, side = 'left', fill = 'both')

        self.scrollbar = tk.Scrollbar(self.framelista) 

         # Selection du premier élément de listbox.
        self.listbox.select_set(0)
  
        # Adding Scrollbar to the right 
        # side of root window 
        self.scrollbar.pack(side = 'right', fill = 'both') 
        self.listbox.bind('<<ListboxSelect>>', self.clic)  ## on associe l'évènement "clic en la lista"
        self.listbox.config(yscrollcommand = self.scrollbar.set) 
  
        # setting scrollbar command parameter  
        # to listbox.yview method its yview because 
        # we need to have a vertical view 
        self.scrollbar.config(command = self.listbox.yview) 
  
        self.frameopciones = tk.Frame( self.frame, bg='#4065A4', bd=1, relief='sunken')

        self.label_mas = tk.Label( self.frameopciones, text = 'Aumentar el stock de: ')
        self.label_mas.pack(pady=5)

        self.campo1 = tk.Entry( self.frameopciones, font=("Arial", 10), bg='darkred', fg='red', borderwidth=0) # Falta borrar lo escrito
        self.campo1.pack(pady=5)

        #self.boton_mas = tk.Button( self.frame, text = 'Validar', command = self.aumentar_stock)
        self.boton_mas = tk.Button( self.frameopciones, text = 'Validar', command = self.agregar_cantidad )
        self.boton_mas.pack(pady=5)

        self.label_menos = tk.Label( self.frameopciones, text = 'Disminuir el stock de: ')
        self.label_menos.pack(pady=5)

        self.campo2 = tk.Entry( self.frameopciones, font=("Arial", 10), bg='darkred', fg='red', borderwidth=0) # Falta borrar lo escrito
        self.campo2.pack(pady=5)

        #self.boton_menos = tk.Button( self.frame, text = 'Validar', command = self.disminuir_stock)
        self.boton_menos = tk.Button( self.frameopciones, text = 'Validar', command = self.disminuir_cantidad )
        self.boton_menos.pack(pady=5)

        #self.boton_verificacion = tk.Button( self.frame, text = 'Desea recuperar el stock del producto?', command = self.verificar_stock)
        self.boton_verificacion = tk.Button( self.frameopciones, text = 'Desea recuperar el stock del producto?')
        self.boton_verificacion.pack(pady=5)

        # Boton para salir de la aplicacion
        #self.bouton_volver = tk.Button( self.frame, text = "Volver al menu", command = self.volver )
        self.bouton_volver = tk.Button( self.frame, text = "Volver al menu" )
        self.bouton_volver.pack(side=tk.BOTTOM, pady=5)

        # Boton para salir de la aplicacion
        #self.bouton_salir = tk.Button( self.frame, text = "Salir", command = self.quit )
        self.bouton_salir = tk.Button( self.frame, text = "Salir" )
        self.bouton_salir.pack(side=tk.BOTTOM, pady=5)

        self.frameopciones.pack(side='right')
        self.framelista.pack(side='left', padx = 5)
    
        self.frame.pack()
    
    def clic(self, event):
        i = self.listbox.curselection()

        producto_lista = self.listbox.get(i)
        #print("le producto seleccionado est", producto_lista)
        
        return producto_lista  ## On retourne l'élément (un string) sélectionné


    def agregar_cantidad(self):
        """ funcion para verificar si se hace un insert o un update """

        alimentos = self.clic(self)
        
        #print( "producto recibido es: ",alimentos)

        alimento = str(alimentos)

        producto = alimento[2:-3]

        #print( "producto modificado es: ",producto)
            
        cantidad  = self.campo1.get()

        interrogacion = []
        interrogacion = [ producto, int(cantidad) ]

        pregunta = "SELECT * FROM ingredientes WHERE nombre = '%s'"%(producto)

        if self.base.consultacion_bis(pregunta):
            """ Vamos a poner al dia la cantidad """
            #print("Solo vamos a poner al dia la cantidad")
            
            self.base.updatemas(interrogacion)
        else:
            """ El producto nuevo se puede agregar """
            #print(" El producto nuevo y se puede agregar en la tabla ingredientes ")
            
            self.base.agregar(interrogacion)

        # si todo salio bien, seguimos
        if True:
            print("el stock esta al dia") # affichar mensaje en la consola

    def disminuir_cantidad(self):
        """ funcion para verificar si se hace un insert o un update """

        alimentos = self.clic(self)
        
        #print( "producto recibido es: ",alimentos)

        alimento = str(alimentos)

        producto = alimento[2:-3]

        #print( "producto modificado es: ",producto)
            
        cantidad  = self.campo2.get()

        interrogacion = []
        interrogacion = [ producto, int(cantidad) ]

        pregunta = "SELECT * FROM ingredientes WHERE nombre = '%s'"%(producto)

        if self.base.consultacion_bis(pregunta):
            """ Vamos a poner al dia la cantidad """
            #print("Solo vamos a poner al dia la cantidad")
            
            self.base.updatemenos(interrogacion)

            if False:
                print("la cantidad pedida es superior a la cantidad en stock") # A completar
        if True:
            print("el stock esta al dia")
        
        #replaceText1()

    #def replaceText1(self, text):
        #self.display1.delete(0, END)
        #self.display1.insert(0, text)
    

class GestionMenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Aquí puedes agregar widgets para la gestión del inventario

class GestionPlatoDiaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Aquí puedes agregar widgets para la gestión del inventario

class GestionInventarioFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Aquí puedes agregar widgets para la gestión del inventario


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
