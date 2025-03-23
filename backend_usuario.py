
""" Configuración de la conexión a la base de datos MySQL
    es realisada en el modulo gestion_bdd """

from flask import Flask, request, jsonify
import gestion_bdd as mibase
import re
from datetime import datetime



def create_app():
    app = Flask(__name__)

    with app.app_context():
        from rutas_usuario import configura_rutas_usuario
        configura_rutas_usuario(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)


