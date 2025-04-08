from flask import Flask, jsonify, request
from entities.encargados import Encargado

app = Flask(__name__)


@app.route('/encargados', methods=['GET'])
def get_encargados():
    encargados = Encargado.get()
    return jsonify(encargados), 200

@app.route('/encargados', methods=['POST'])
def save_encargado():
    data = request.json
    encargado = Encargado(
        puesto=data['puesto'],
        nombre=data['nombre'],
        telefono=data.get('telefono')
    )
    result = Encargado.save(encargado)
    success = isinstance(result, int)
    return jsonify({"success": success, "id": result}), 201 if success else 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)