from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Lista para almacenar los usuarios registrados
usuarios_registrados = []

@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    nuevo_usuario = {
        'nombre': user_data['nombre'],
        'apellidoPaterno': user_data['apellidoPaterno'],
        'apellidoMaterno': user_data['apellidoMaterno'],
        'email': user_data['email']
    }
    usuarios_registrados.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

@app.route('/users', methods=['GET'])  # Cambiar a GET para obtener usuarios
def get_users():
    return jsonify(usuarios_registrados), 200

if __name__ == '__main__':
    app.run(debug=True)
