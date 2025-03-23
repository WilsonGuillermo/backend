""" Archivo `app.py`

Este archivo es el punto de entrada principal de tu aplicación. Configura la aplicación Flask y ejecuta el servidor.

"""

from flask import Flask
from modelos import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://majo:WilsonMemo_1964@localhost/boutique'
    db.init_app(app)

    with app.app_context():
        from routes import configure_routes
        configure_routes(app)
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001, debug=True)
