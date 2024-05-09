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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
