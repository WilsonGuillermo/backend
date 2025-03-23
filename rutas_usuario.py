
""" Configuración de la conexión a la base de datos MySQL
    es realisada en el modulo gestion_bdd """

from flask import Flask, request, jsonify
import gestion_bdd as mibase
import re
from datetime import datetime

def configura_rutas_usuario(app):

    def is_valid_password(password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    def is_valid_login(login):
        requete = "select count(*) from usuarios where nombre_usuario = '%s'"%login

        print("la requete es :", requete)

        bdd = mibase.mi_base()

        papel = bdd.verificacion_usuario(requete)

        if papel[0] == 0:
            return True
        else:
            return False

    @app.route('/verificarCuenta/<login>', methods=['GET'])
    def verificarCuenta(login):

        #usuario = request.json['login']

        print("el valor a enviar ahora mismo es: %s"%login)

        requete = "select count(*) as count from usuarios where nombre_usuario = '%s'"%login

        print("la requete es : %s"%requete)
        
        bdd = mibase.mi_base()

        papel = bdd.verificacion_usuario(requete)

        print("lo recuperado es")

        print(papel)


        if papel[0] == 0:
            return jsonify({"continuar creacion": "Login valido"}), 200
        else:
            return jsonify({"error": "Login already exists"}), 409

    @app.route('/agregarCuenta', methods=['POST'])
    def agregarCuenta():
        # Creacion de la cuenta utilisador
        try:
            data = request.get_json()

            print(data)

            nombre = request.json['name']

            apellido = request.json['surname']

            nombre_usuario = request.json['login']

            contrasena = request.json['password']

            fecha_de_nacimiento = request.json['birth_date']

            email = request.json['email']

            rol = request.json['role']

            creacion_date = datetime.now()
            #requete = "insert into usuarios (nombre, apellido, nombre_usuario, email, contrasena, fecha_de_nacimiento, rol) values (%s,%s,%s,%s,%s,%s,%s)"%(nombre, apellido, nombre_usuario, email, contrasena, fecha_de_nacimiento, rol)

            #print("la requete es :", requete)

            if not all([nombre, apellido, nombre_usuario, email, contrasena, fecha_de_nacimiento, rol]):
                return jsonify({"error": "Todos los campos son obligatorios"}), 400

            if not is_valid_password(contrasena):
                print(contrasena)
                return jsonify({"error": "Invalid password"}), 400

            if not is_valid_login(nombre_usuario):
                return jsonify({"error": "Login already exists"}), 409
            
            requete = "insert into usuarios (nombre, apellido, nombre_usuario, email, contrasena, fecha_de_nacimiento, rol, fecha_creacion_cuenta) values ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(nombre, apellido, nombre_usuario, email, contrasena, fecha_de_nacimiento, rol, creacion_date)

            print("la requete bis es :", requete)

            bdd = mibase.mi_base()

            bdd.creacion_usuario(requete)

                # El usuario a sido creado
            return jsonify({"message": "User created successfully"}), 201
                # return jsonify({'user_id': user['id'], 'username': user['username'], 'email': user['email']})
        except Exception as e:
            # Si el usuario no ha sido creado, retornar un mensaje de error
            return jsonify({'error': str(e)}), 400

    @app.route('/login', methods=['POST'])
    def login():
        # Obtener los datos del formulario enviado en la solicitud
        
        usuario = request.json['username']

        contrasena  = request.json['password']

        print("el valor a enviar ahora mismo es: ",usuario," y ", contrasena)

        requete = "select rol from usuarios where nombre_usuario = '%s' and contrasena = '%s'"%(usuario,contrasena)

        print("la requete es :", requete)
        
        bdd = mibase.mi_base()

        papel = bdd.consultacion_usuario(requete)
        
        print("le profil es: ",papel)

        if papel:
            # Si el usuario existe, retornar sus datos
            return jsonify({'usuario': usuario, 'contrasena': contrasena, 'profil': papel})
            #return jsonify({'user_id': user['id'], 'username': user['username'], 'email': user['email']})
        else:
            # Si el usuario no existe, retornar un mensaje de error
            return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401

    @app.route('/ingredientes_referencial', methods=['GET'])
    def ingredientes_referencial():
        # Aquí iría tu lógica para buscar ingredientes
        # Usar request.args para obtener los parámetros de la consulta (query string)
        requete = "select nombre from referencia_ingredientes"

        print("la requete es :", requete)
        
        bdd = mibase.mi_base()

        lista_productos = bdd.consultacion_generique(requete)
            
        print("los productos son: ",lista_productos)

        if lista_productos:
            # Si el usuario existe, retornar sus datos
            return jsonify(productos=lista_productos)
            #return jsonify({'user_id': user['id'], 'username': user['username'], 'email': user['email']})
        else:
            # Si el usuario no existe, retornar un mensaje de error
            return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401

    @app.route('/roles', methods=['GET'])
    def roles():
        # Aquí iría tu lógica para buscar ingredientes
        # Usar request.args para obtener los parámetros de la consulta (query string)
        requete = "select * from roles"

        print("la requete es :", requete)
        
        bdd = mibase.mi_base()

        lista_roles = bdd.consultacion_generique(requete)

        roles_ok = [{"id" : roles[0], "role": roles[1]} for roles in lista_roles]
            
        print("los roles son: ",roles_ok)

        if lista_roles:
            # Si el usuario existe, retornar sus datos
            return jsonify(roles_ok)
            #return jsonify({'user_id': user['id'], 'username': user['username'], 'email': user['email']})
        else:
            # Si el usuario no existe, retornar un mensaje de error
            return jsonify({'error': 'No hay profiles!!'}), 401
            
    @app.route('/cantidadProducto', methods=['POST'])
    def cantidadProducto():
        # Obtener los datos del formulario enviado en la solicitud
        
        nombre = request.json['producto']

        cantidad = request.json['cantidad']

        accion = request.json['accion']

        producto_al_dia = ( nombre, cantidad, accion)

        bdd = mibase.mi_base()

        print("la cantidad para modificar el stock del producto ", nombre," es : ",cantidad)
        
        resultado = bdd.updatemasomenos(producto_al_dia)  
        
        print("Despues requete, lo recibido es: ",resultado)
        print("Despues requete, el mensaje recibido es %s: "%resultado[1])

        if resultado != "problema":
            if resultado[1] != "No hay stock disponible":
                if resultado[1] != "El stock no es suficiente":
                    respuesta = resultado[0]

                    nombre = respuesta[0]

                    cantidad = respuesta[1]

                    ejecutado = "OK"

                    # Todo salio bien
                    print("el mensaje recibido es %s: "%resultado[1])
                    return jsonify({'producto': nombre},{'cantidad': cantidad},{'resultado': ejecutado})
                else:
                    respuesta = resultado[0]

                    nombre = respuesta[0]

                    cantidad = respuesta[1]

                    ejecutado = "KO_1"
                    print("el mensaje recibido es %s: "%resultado[1])
                    return jsonify({'producto': nombre},{'cantidad': cantidad}, {'resultado': ejecutado}), 401
            else:
                ejecutado = "KO_2"
                print("el mensaje recibido es %s: "%resultado[1])
                return jsonify({'producto': nombre},{'cantidad': cantidad}, {'resultado': ejecutado}), 401
        else:
            # Si por alguna razon, el producto no puede ponerse al dia, retornar un mensaje de error
            return jsonify({'error': 'La cantidad no pudo ponerse al dia'}), 401

    @app.route('/stockProducto', methods=['POST'])
    def stockProducto():
        # Obtener los datos del formulario enviado en la solicitud
        
        nombre = request.json['producto']

        accion = request.json['accion']

        producto_al_dia = (nombre, accion)

        bdd = mibase.mi_base()

        print("Vamos a solicitar el stock del producto ", nombre)

        print("llamamos la funcion consultacionStock")
        
        resultado = bdd.consultacionStock(producto_al_dia)
        
        print("Despues requete, lo recibido es: ",resultado)
        #print("Despues requete, el mensaje recibido es %s: "%resultado[1])

        if accion == "Unico":

            print("aqui estoy, Unico")
            
            if resultado is None:
                return jsonify({'error': 'El producto no esta en stock'}), 401
            else:
                #respuesta = resultado[0]

                nombre = resultado[0]

                cantidad = resultado[1]

                ejecutado = "OK"

                #cantidad = resultado[1]

                # Todo salio bien
                return jsonify({'producto': nombre},{'cantidad': cantidad},{'resultado': ejecutado})
                    
        else:
            if accion == "Todo":
                return jsonify(resultado)
            else:
                # Si por alguna razon, el producto no puede ponerse al dia, retornar un mensaje de error
                return jsonify({'error': 'La cantidad no pudo ponerse al dia'}), 401

