""" Archivo `routes.py`

Este archivo define las rutas y la lógica del manejo de las solicitudes. Importa y usa la aplicación Flask configurada en `app.py`.

"""
from flask import Flask, request, jsonify
from modelos import db, Category, Product, Image
import json

##from flask import request, jsonify
##from modelos import db, Product

def configure_routes(app):

    @app.route('/categories', methods=['GET', 'POST'])
    def manage_categories():
        if request.method == 'POST':
            data = request.json
            new_category = Category(name=data['name'], description=data['description'])
            db.session.add(new_category)
            db.session.commit()
            return jsonify(new_category), 201
        else:
            categories = Category.query.all()
            return jsonify([c.to_dict() for c in categories])

    @app.route('/products', methods=['GET', 'POST'])
    def manage_products():
        if request.method == 'POST':
            data = request.json
            new_product = Product(
                name=data['name'],
                description=data['description'],
                price=data['price'],
                category_id=data['category_id'],
                size=data['size'],
                color=data['color'],
                stock=data['stock']
            )
            db.session.add(new_product)
            db.session.commit()
            return jsonify(new_product), 201
        else:
            products = Product.query.all()
            return jsonify([p.to_dict() for p in products])

    @app.route('/products/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
    def manage_product(product_id):
        product = Product.query.get_or_404(product_id)
        if request.method == 'GET':
            return jsonify(product.to_dict())
        elif request.method == 'PUT':
            data = request.json
            product.name = data['name']
            product.description = data['description']
            product.price = data['price']
            product.category_id = data['category_id']
            product.size = data['size']
            product.color = data['color']
            product.stock = data['stock']
            db.session.commit()
            return jsonify(product.to_dict())
        elif request.method == 'DELETE':
            db.session.delete(product)
            db.session.commit()
            return '', 204
