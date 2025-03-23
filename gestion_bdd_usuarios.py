""" Modulo Uusarios """
""" Version 4, proyecto ANYEA """
""" WgMg Python ChatPT """
""" Gestion de usuarios """

### Session de imports
import mysql.connector as base

class mi_base(object):
    # Conectarse a la BDD
    def __init__(self):
        
        self.conexion = base.connect(
            host = "localhost",
            user = "majo",
            password = "WilsonMemo_1964",
            database = "boutique"
        )

        # Crear un cursor para ejecutar consultas "
        self.cursor = self.conexion.cursor()

    # Ejecutar insercion: Agregar un producto
    def agregar(self, producto):
        """ Agregando ingrediente """

        print("el producto recibido para agregar es: ", producto)

        agregando = "insert into ingredientes (nombre, cantidad, fecha_vencimiento) VALUES ('%s', %s, '2027-12-12')"%(producto[0],producto[1])
        
        #data = producto

        #requete = agregando%data
        print("el producto recibido para agregar es: ", producto)
        print("la requete es: ", agregando)

        self.ejecutar_requete(agregando)
        self.ejecutar_requete("commit")

    def creacion_usuario(self, usuario):
        """ Agregando usuario """

        print("el usuario recibido para agregar es: ", usuario)

        #agregando_usuario = "insert into usuarios (nombre, apellido, nombre_usuario, contrasena, fecha_nacimiento, mail, perfil ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"%( usuario[0], usuario[1], usuario[2], cryptar_password(usuario[3]), usuario[4], usuario[5], usuario[6] )
        
        #print("el candidato recibido para agregar es: ", usuario)
        #print("la requete es: ", agregando_usuario)

        self.ejecutar_requete(usuario)
        self.ejecutar_requete("commit")

        
    # Convertir el segundo elemento de una lista de decimal a una cadena de caracteres
    def convertir_decimales_a_cararacteres(self, lista):
        nueva_lista = []
        for tupla in lista:
            nuevo_elemento = ( tupla[0], str(tupla[1])) # convertir el segundo elemento en cadena de caracteres
            nueva_lista.append(nuevo_elemento)
        return nueva_lista

    # Ejecutar consulta: recuperar la lista de productos
    def consultacionStock(self):

        print("________________TODOS LOS PRODUCTOS___________________")

        #consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, i.url as image_url, p.tipo, t.clase as referencia from productos p LEFT JOIN imagenes i, referencias t ON p.id = i.product_id and p.referencia = t.idreferencias"
        consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, p.imagen, p.tipo, p.referencia, p.estilo, p.corte from boutique.productos p"

        print("la requete es........................")
        print(consulta)

        print("________________TODOS LOS PRODUCTOS BIS__________________")
        
        self.ejecutar_requete(consulta)
        
        resultados = self.cursor.fetchall() # a voir!!!
        
        
        #for fila in resultados:
            #print("________________CADA PRODUCTO ES__________________")

        #    print(fila)

        return resultados
            
    # Ejecutar consulta: recuperar la lista de productos
    def consultacionStockCategoria(self, categoria_id):

        print("la demanda es........", categoria_id)          

        if categoria_id :

            print("-------------------CATEGORIA-UNICA----------------")
        
            #consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, i.url as image_url, p.tipo, t.clase as referencia from productos p LEFT JOIN imagenes i, referencias t ON p.id = i.product_id where and p.referencia = t.idreferencias and p.category_id = '%s'"%categoria_id
            consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, p.imagen, p.tipo, p.referencia, p.estilo, p.corte from boutique.productos p where p.category_id = '%s'"%categoria_id

            print(consulta)
            
            self.ejecutar_requete(consulta)
            
            resultados = self.cursor.fetchall() # a voir!!!
            
            
            for fila in resultados:
                print(fila)

            return resultados
        
        else:

            print("________________TODAS LAS CATEGORIAS___________________")

            #consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, i.url as image_url, p.tipo, t.clase as referencia from productos p LEFT JOIN imagenes i, referencias t ON p.id = i.product_id and p.referencia = t.idreferencias"
            consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, p.imagen, p.tipo, p.referencia, p.estilo, p.corte from boutique.productos p"

            self.ejecutar_requete(consulta)

            # Obtener los resultados
            resultados = self.cursor.fetchall() # a voir!!!
            
            for fila in resultados:
                print(fila)

            return resultados
    
    # Ejecutar consulta: recuperar la lista de productos
    def consultacionStockTipo(self, tipo, category_id):
                
        print("la demanda es........", tipo, category_id) 

        if int(category_id) != 0 :

            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
        
            #consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, i.url as image_url, p.tipo, t.clase as referencia from productos p LEFT JOIN imagenes i, referencias t ON p.id = i.product_id where and p.referencia = t.idreferencias and p.category_id = '%s'"%categoria_id
            consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, p.imagen, p.tipo, p.referencia, p.estilo, p.corte from boutique.productos p where p.tipo = '%s' and p.category_id = %i"%(tipo, int(category_id))
                                                                                                                                                     
            #requete = consulta%(tipo, category_id)

            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")
            print("-------------------TIPO-UNICO----------------")

            print(consulta)
            
            self.ejecutar_requete(consulta)
            
            resultados = self.cursor.fetchall() # a voir!!!
            
            
            for fila in resultados:
                print(fila)

            return resultados
        
        else:

            print("________________TODOS LOS TIPOS___________________")

            #consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, i.url as image_url, p.tipo, t.clase as referencia from productos p LEFT JOIN imagenes i, referencias t ON p.id = i.product_id and p.referencia = t.idreferencias"
            consulta = "select p.id, p.name, p.description, p.price, p.category_id, p.size, p.color, p.stock, p.imagen, p.tipo, p.referencia, p.estilo, p.corte from boutique.productos p"

            self.ejecutar_requete(consulta)

            # Obtener los resultados
            resultados = self.cursor.fetchall() # a voir!!!
            
            for fila in resultados:
                print(fila)

            return resultados
            

    # Ejecutar consulta: recuperar la lista de productos
    def consultacion(self):
        consulta = "select * from ingredientes"

        self.ejecutar_requete(consulta)

        # Obtener los resultados
        resultados = self.cursor.fetchall() # a voir!!!
        for fila in resultados:
            print(fila)

    def consultacion_generique(self, interrogation):
        #consulta = "select * from ingredientes"

        self.ejecutar_requete(interrogation)

        # Obtener los resultados
        resultados = self.cursor.fetchall() # a voir!!!

        return resultados

    # Ejecutar consulta simple : verificar si un elemento esta en una tabla
    def consultacion_bis(self, interrogacion):
        
        print("la consultacion es :", interrogacion)
        self.ejecutar_requete(interrogacion)

        resultado = self.cursor.fetchone()
        print("lo q encontro es: ",resultado)
        if resultado is None:
            print("el elemento no esta en la tabla")
            return False
        else:
            print("el elemento si esta en la tabla")
            return True
    
        
    # Ejecutar consulta simple
    def consultacion_usuario(self, usuario):
        print("la consultacion es : %s"%usuario)
        self.ejecutar_requete(usuario)
        #self.cursor.execute(producto)

        resultado = self.cursor.fetchone()
        print("lo q encontro es: %s"%resultado)

        if resultado is None:
            print("la interrogacion no esta: %s"%usuario)
            return False
        else:
            print("la interrogacion esta: %s"%usuario)

        print("le rol es: %s"%resultado[0])
            #return True
        return resultado[0]
    
    def suprimer_usuario(self, usuario):
        print("Vamos a suprimir el usuario : %s"%usuario)
        self.ejecutar_requete(usuario)

        self.ejecutar_requete("commit")

        return '', 204
        
    # Ejecutar consulta simple
    def consultacion_referencial(self, producto):
        consulta = "select nombre from referencia_ingredientes where nombre = '%s'"%producto
        print("la consultacion es :", consulta)
        self.cursor.execute(consulta)

        resultado = self.cursor.fetchone()
        print("Si se encontro en el referencial el producto: ",resultado)
        if resultado is None:
            return False
        else:
            return True
    
    def consultacion_ter(self, producto):
        """ Verifiquemos primero si el producto existe"""

        cantidad = ''  

        consulta = "select nombre from ingredientes where nombre = '%s'"%producto
        print("la consultacion buscando el producto inicial es :", consulta)
        self.ejecutar_requete(consulta)
        presente = self.cursor.fetchone()
        print("la consultacion inicial nos da :", presente)
        if presente is None:
            cantidad = "vacia"  
        else:
            """ si existe, regresamos la cantidad"""
            consulta = "select cantidad from ingredientes where nombre = '%s'"%producto
            print("la consultacion para escojer la cantidad :", consulta)
            self.ejecutar_requete(consulta)

            cantidad = float(self.cursor.fetchone()[0])
            print("lo q encontro es: ",cantidad)

        return cantidad
        


    # Ejecutar maj
    def updatemasomenos(self, producto):
        """ Actualizando ingrediente """
        mensaje = ''
        data = producto
        print("el producto recibido es: ", producto[0]," y ",producto[1])

        cantidad_actual = self.consultacion_ter(producto[0])

        print("la cantidad obtenida es", cantidad_actual)

        try:
            if cantidad_actual == "vacia":
                if producto[2] == "Aumentar":
                    self.agregar(producto)
                    print("no habia nada")
                    mensaje = "Cantidad modificada correctamente"
                else:
                    mensaje = "No hay stock disponible" 
                    print("no habia nada, no se puede disminuir")  
            else:
                if producto[2] == "Aumentar":
                    nueva_cantidad = float(producto[1]) + float(cantidad_actual)
                    print("habia algo, se aumenta")  
                    actualizando = "update ingredientes set cantidad = %3i, fecha_vencimiento = '2028-10-10' where nombre = '%s'"
                
                    requete = actualizando%(int(nueva_cantidad),producto[0])
                    print("la requete es: ", requete)
                    self.ejecutar_requete(requete)
                    self.ejecutar_requete("commit")
                    mensaje = "Cantidad modificada correctamente"

                elif producto[2] == "Disminuir":
                    if cantidad_actual < float(producto[1]):
                        mensaje = "El stock no es suficiente" # envoyer stock actual
                        print("no hay suficiente, no se puede disminuir")  
                    else:
                        nueva_cantidad =  float(cantidad_actual) - float(producto[1])
                        print("hay suficiente, se puede disminuir")
                        actualizando = "update ingredientes set cantidad = %3i, fecha_vencimiento = '2028-10-10' where nombre = '%s'"
                
                        requete = actualizando%(int(nueva_cantidad),producto[0])
                        print("la requete es: ", requete)
                        self.ejecutar_requete(requete)
                        self.ejecutar_requete("commit")  
                        mensaje = "Cantidad modificada correctamente"

            retorno = "select nombre, cantidad from ingredientes where nombre = '%s'"%producto[0]
            self.ejecutar_requete(retorno)
            return (self.cursor.fetchone(),mensaje)
        except:
            return "problema"  

    # Ejecutar maj
    def updatemenos(self, producto):
        """ disminuyendo cantidad ingrediente """
        data = producto
        print("el producto recibido es: ", producto[0]," y ",producto[1])

        cantidad_actual = self.consultacion_ter(producto[0])

        if cantidad_actual < producto[1]:
            return False
        else:
            nueva_cantidad = cantidad_actual - producto[1]

            actualizando = "update ingredientes set cantidad = %3i, fecha_vencimiento = '2028-10-10' where nombre = '%s'"

            requete = actualizando%(int(nueva_cantidad),producto[0])

            print("la requete es: ", requete)

            self.ejecutar_requete(requete)

            self.ejecutar_requete("commit")

            if cantidad_actual == producto[1]:
        
                borrar_linea = "DELETE FROM ingredientes WHERE nombre = '%s'"%(producto[0])

                self.ejecutar_requete(borrar_linea)

                self.ejecutar_requete("commit")
        
    # Ejecutar requete y verificar sino hay error
    def ejecutar_requete(self, interrogacion ):
        """ Funcion que nos va a ejecutar las requetes y
            nos va a verificar si hay un error o no """
        
        try:
            self.cursor.execute(interrogacion)
        except base.Error as e:
            print("Error al ejecutar la consulta", e)

    def fin(self):
        self.cursor.close()
        self.conexion.close()


### Session principal
if __name__ == "__main__" :
    #controlando = Kontrolador()
    probando = mi_base()
    probando.consultacion_usuario("select nombre_usuario from usuarios where nombre_usuario = 'felipe'")
    #probando.update()
    probando.consultacion()
    probando.fin()
    #probando.gestion_del_menu()
    
