""" Configuración de la conexión a la base de datos MySQL
    es realisada en el modulo gestion_bdd """

from flask import Flask, request, jsonify
import gestion_bdd_productos as mibase
import re
from datetime import datetime
#from modelos import Categoria, Producto, Imagen

app = Flask(__name__)


@app.route('/categorias', methods=['GET', 'POST'])
def manage_categorias():

    db = mibase.mi_base()

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
        requete = "select * from categorias"

        print("la requete es :", requete)
        
        #bdd = mibase.mi_base()

        lista_categorias = db.consultacion_generique(requete)

        categorias_ok = [{"id" : roles[0], "name": roles[1], "description": roles[2]} for roles in lista_categorias]
        #categorias_ok = [{"id" : roles[0], "name": roles[1]} for roles in lista_categorias]
            
        print("las categorias son: ",categorias_ok)

        if lista_categorias:
            # Si el usuario existe, retornar sus datos
            return jsonify(categorias_ok)
            #return jsonify({'user_id': user['id'], 'username': user['username'], 'email': user['email']})
        else:
            # Si el usuario no existe, retornar un mensaje de error
            return jsonify({'error': 'No hay categorias!!'}), 401
            print('----------------9-----------')
        #return jsonify([c.to_dict() for c in categorias])

@app.route('/productos', methods=['GET', 'POST'])
def manage_productos():

    db = mibase.mi_base()

    if request.method == 'POST':
        data = request.json
        new_product = Producto(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category_id=data['category_id'],
            size=data['size'],
            color=data['color'],
            stock=data['stock'],
            tipo=data['tipo'],
            referencia=data['referencia'],
            estilo=data['estilo'],
            corte=data['corte']
        )
        db.session.add(new_producto)
        db.session.commit()
        return jsonify(new_producto), 201
    else:
        lista_productos = db.consultacionStock()

        #print("estoy en productos..............los productos son: ",lista_productos)

        productos_ok = [{"id" : campo[0], "name": campo[1], "description": campo[2], "price": campo[3], "categoryId": campo[4], "size": campo[5], "color": campo[6], "stock": campo[7], "imagen": campo[8], "tipo": campo[9], "referencia": campo[10], "estilo": campo[11], "corte": campo[12]} for campo in lista_productos]
        
        #print("estoy en productos..............los productos son: ",productos_ok)

        if lista_productos:
        
            return jsonify(productos_ok)
            
        else:
        
            return jsonify({'error': 'No hay categorias!!'}), 401
    
@app.route('/productos_par_categoria', methods=['GET'])
def get_products():

    db = mibase.mi_base()

    category_id = request.args.get('category_id')
    #db.consultacionStockCategoria

    lista_productos = db.consultacionStockCategoria(category_id)

    #print("estoy en products................los productos por categoria son: ",lista_productos)

    productos_ok = [{"id" : campo[0], "name": campo[1], "description": campo[2], "price": campo[3], "categoryId": campo[4], "size": campo[5], "color": campo[6], "stock": campo[7], "imagen": campo[8], "tipo": campo[9], "referencia": campo[10], "estilo": campo[11], "corte": campo[12]} for campo in lista_productos]
    
    #print("estoy en productos_par_categoria................los productos son: ",productos_ok)

    if lista_productos:
    
        return jsonify(productos_ok)
        
    else:
    
        return jsonify({'error': 'No hay categorias!!'}), 401


@app.route('/producto/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_producto(product_id):

    db = mibase.mi_base()
    
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
        producto.tipo = data['tipo']
        producto.referencia = data['referencia']
        db.session.commit()
        return jsonify(producto.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(producto)
        db.session.commit()
        return '', 204


@app.route('/productos_par_tipo', methods=['POST'])
def get_productos_tipo():
    # Obtener los datos del formulario enviado en la solicitud
    
    db = mibase.mi_base()

    tipo = request.json['tipo']

    category_id  = request.json['category_id']

    lista_productos = db.consultacionStockTipo(tipo, category_id)

    #print("estoy en products................los productos por categoria son: ",lista_productos)

    productos_ok = [{"id" : campo[0], "name": campo[1], "description": campo[2], "price": campo[3], "categoryId": campo[4], "size": campo[5], "color": campo[6], "stock": campo[7], "imagen": campo[8], "tipo": campo[9], "referencia": campo[10], "estilo": campo[11], "corte": campo[12]} for campo in lista_productos]
    
    print("estoy en productos_por_tipo................los productos son: ",productos_ok)

    if lista_productos:
    
        return jsonify(productos_ok)
        
    else:
    
        return jsonify({'error': 'No hay tipos!!'}), 401
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
