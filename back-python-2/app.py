# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

# Crear la aplicación Flask
app = Flask(__name__)

# Permitir CORS
CORS(app)

# Lista para almacenar las asignaciones de eventos
asignaciones = []

# Ruta para asignar un evento a un usuario
@app.route('/asignarEvento', methods=['POST'])
def asignar_evento():
    data = request.get_json()
    usuario = data.get('usuario')
    evento = data.get('evento')

    # Agregar la asignación a la lista
    asignaciones.append({'usuario': usuario, 'evento': evento})

    return jsonify({'message': 'Evento asignado exitosamente', 'usuario': usuario, 'evento': evento}), 201

# Ruta para obtener todas las asignaciones
@app.route('/asignaciones', methods=['GET'])
def obtener_asignaciones():
    return jsonify(asignaciones)

if __name__ == '__main__':
    app.run(port=5500)
