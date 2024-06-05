
""" Configuración de la conexión a la base de datos MySQL
    es realisada en el modulo gestion_bdd """

from flask import Flask, request, jsonify
import gestion_bdd as mibase

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos del formulario enviado en la solicitud
    
    usuario = request.json['username']

    contrasena  = request.json['password']

    print("el valor a enviar ahora mismo es: ",usuario," y ", contrasena)

    requete = "select * from usuarios where nombre_usuario = '%s' and contrasena = '%s'"%(usuario,contrasena)

    print("la requete es :", requete)
    
    bdd = mibase.mi_base()

    papel = bdd.consultacion_usuario(requete)
    
    print("le profil es: ",papel)

    ###############################""
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
    #query = request.args.get('q')
    #return jsonify([{'id': '1', 'name': 'Ingrediente 1'}, {'id': '2', 'name': 'Ingrediente 2'}])

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

    ###############################""
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

    producto_al_dia = ( nombre, accion)

    bdd = mibase.mi_base()

    print("Vamos a solicitar el stock del producto ", nombre,)
    
    resultado = bdd.consultacionStock(producto_al_dia)
    
    print("Despues requete, lo recibido es: ",resultado)
    #print("Despues requete, el mensaje recibido es %s: "%resultado[1])

    ###############################""
    if accion == "Unico":

        if resultado is None:
            return jsonify({'error': 'El producto no esta en stock'}), 401
        else:
            #respuesta = resultado[0]

            nombre = resultado[0]

            cantidad = resultado[1]

            ejecutado = "OK"

            #cantidad = resultado[1]

            # Todo salio bien
            #print("el mensaje recibido es %s: "%resultado)
            return jsonify({'producto': nombre},{'cantidad': cantidad},{'resultado': ejecutado})
                
    else:
        if accion == "Todo":
            return jsonify(resultado)
        else:
            # Si por alguna razon, el producto no puede ponerse al dia, retornar un mensaje de error
            return jsonify({'error': 'La cantidad no pudo ponerse al dia'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
