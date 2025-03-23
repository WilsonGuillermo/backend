"""
    Crea un archivo `populate_db.py` para agregar datos de prueba a las tablas.
"""
from modelos import db, Categoria, Producto, Imagen
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://majo:WilsonMemo_1964@localhost/boutique'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def populate_db():
    app = create_app()
    with app.app_context():
        # Agregar categorías de ejemplo
        categories = [
            Categoria(name='Ropa Femenina'),
            Categoria(name='Ropa Masculina')
        ]
        db.session.add_all(categories)
        db.session.commit()

        # Agregar productos de ejemplo
        products = [
            Producto(name='Vestido Rojo', description='Vestido de verano', price=49.99, category_id=1, size='M', color='Rojo', stock=10),
            Producto(name='Camisa Azul clara', description='Camisa casual', price=29.99, category_id=2, size='L', color='Azul', stock=15),
            Producto(name='Vestido Blanco', description='Vestido de verano', price=49.99, category_id=1, size='M', color='Rojo', stock=10),
            Producto(name='Camisa Rosada', description='Camisa casual', price=29.99, category_id=2, size='L', color='Azul', stock=15),
            Producto(name='Vestido Amarillo', description='Vestido de verano', price=49.99, category_id=1, size='M', color='Rojo', stock=10),
            Producto(name='Camisa Blanca', description='Camisa casual', price=29.99, category_id=2, size='L', color='Azul', stock=15),
            Producto(name='Vestido Largo', description='Vestido de verano', price=49.99, category_id=1, size='M', color='Rojo', stock=10),
            Producto(name='Falda de colores', description='Camisa casual', price=29.99, category_id=2, size='L', color='Azul', stock=15),
            Producto(name='Vestido Corto Azul', description='Vestido de verano', price=49.99, category_id=1, size='M', color='Rojo', stock=10)
        ]
        db.session.add_all(products)
        db.session.commit()

        # Agregar imágenes de ejemplo
        images = [
            Imagen(product_id=1, url='https://th.bing.com/th/id/OLC.GvENwSFhFW5ChQ480x360?&rs=1&pid=ImgDetMain'),
            Imagen(product_id=2, url='https://maribelarangonovias.com/wp-content/uploads/2020/11/MG_9930.jpg'),
            Imagen(product_id=3, url='https://th.bing.com/th?id=OLC.w4A/SbSSI/Zabw480x360&rs=1&pid=ImgDetMain'),
            Imagen(product_id=4, url='https://maribelarangonovias.com/wp-content/uploads/2020/09/doce.jpg'),
            Imagen(product_id=5, url='https://th.bing.com/th/id/OLC.gYfgB4IYmcVFig480x360?&rs=1&pid=ImgDetMain'),
            Imagen(product_id=6, url='https://th.bing.com/th?id=OLC.rnJ8dmyxA+wZxA480x360&rs=1&pid=ImgDetMain'),
            Imagen(product_id=7, url='https://th.bing.com/th/id/OLC.sVc64BRWRsWI2g480x360?&rs=1&pid=ImgDetMain'),
            Imagen(product_id=8, url='https://th.bing.com/th?id=OLC.ls9L+5+CHEqGMA480x360&rs=1&pid=ImgDetMain'),
            Imagen(product_id=9, url='https://th.bing.com/th/id/OLC.vkP0MvMuYYqfjg480x360?&rs=1&pid=ImgDetMain'),
        ]
        db.session.add_all(images)
        db.session.commit()

if __name__ == '__main__':
    populate_db()
