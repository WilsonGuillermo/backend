from flask_sqlalchemy import SQLAlchemy
from backend_producto import dbase

db = dbase

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    print('----------------10-----------')

    def to_dict(self):
        print('----------------11-----------')
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    size = db.Column(db.String(50))
    color = db.Column(db.String(50))
    stock = db.Column(db.Integer)
    category = db.relationship('Categoria', backref=db.backref('productos', lazy=True))

class Imagen(db.Model):
    __tablename__ = 'imagenes'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    url = db.Column(db.String(255))
    product = db.relationship('Producto', backref=db.backref('imagenes', lazy=True))
