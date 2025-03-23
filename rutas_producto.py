""" Archivo `routes.py`

Este archivo define las rutas y la lógica del manejo de las solicitudes. Importa y usa la aplicación Flask configurada en `app.py`.

"""
from flask import Flask, request, jsonify
from flask import Blueprint
from modelos import Categoria, Producto, Imagen
from backend_producto import dbase
from flask_sqlalchemy import SQLAlchemy

import json

##from flask import request, jsonify
##from modelos import db, Product

#def configura_rutas_producto(app):
bp = Blueprint('main', __name__)
    
print('----------------3-----------')
db = dbase
print('----------------4-----------')

@bp.route('/categorias', methods=['GET', 'POST'])
def manage_categorias():
    print('----------------5-----------')
    if request.method == 'POST':
        print('----------------7-----------')
        data = request.json
        new_categoria = Categoria(name=data['name'], description=data['description'])
        db.session.add(new_categoria)
        db.session.commit()
        return jsonify(new_categoria), 201
    else:
        print('----------------6-----------')
        categorias = Categoria.query.all()
        print('----------------9-----------')
        return jsonify([c.to_dict() for c in categorias])

@bp.route('/productos', methods=['GET', 'POST'])
def manage_productos():
    if request.method == 'POST':
        data = request.json
        new_product = Producto(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category_id=data['category_id'],
            size=data['size'],
            color=data['color'],
            stock=data['stock']
        )
        db.session.add(new_producto)
        db.session.commit()
        return jsonify(new_producto), 201
    else:
        productos = Producto.query.all()
        return jsonify([p.to_dict() for p in productos])
    
@bp.route('/products', methods=['GET'])
def get_products():
    category_id = request.args.get('category_id')
    if category_id:
        productos = Producto.query.filter_by(category_id=category_id).all()
    else:
        productos = Producto.query.all()
    return jsonify([producto.to_dict() for producto in productos])


@bp.route('/producto/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_producto(product_id):
    producto = Producto.query.get_or_404(product_id)
    if request.method == 'GET':
        return jsonify(producto.to_dict())
    elif request.method == 'PUT':
        data = request.json
        producto.name = data['name']
        producto.description = data['description']
        producto.price = data['price']
        producto.category_id = data['category_id']
        producto.size = data['size']
        producto.color = data['color']
        producto.stock = data['stock']
        db.session.commit()
        return jsonify(producto.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(producto)
        db.session.commit()
        return '', 204
