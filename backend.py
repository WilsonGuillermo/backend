""" programa Python para crear my backend """

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Aquí iría tu lógica para autenticar al usuario y devolver los datos del menú
    # Usar request.json para obtener los datos enviados en la solicitud
    return jsonify({'user_id': '123', 'menu': ['plato1', 'plato2']})

@app.route('/ingredients', methods=['GET'])
def search_ingredients():
    # Aquí iría tu lógica para buscar ingredientes
    # Usar request.args para obtener los parámetros de la consulta (query string)
    query = request.args.get('q')
    return jsonify([{'id': '1', 'name': 'Ingrediente 1'}, {'id': '2', 'name': 'Ingrediente 2'}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

