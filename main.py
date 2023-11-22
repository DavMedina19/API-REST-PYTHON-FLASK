#API REST CREADA CON PYTHON Y FLASK. BY: HECTOR MEDINA Y GUSTAVO ORTEGA.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Método GET para obtener datos de un usuario
@app.route("/users/<user_id>")
def get_user(user_id):
    # Simulación de datos de usuario
    user = {"id": user_id, "nombre": "test", "codigo estudiantil": "999.888.777"}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

# Método POST para crear un nuevo usuario
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    # Simplemente se agrega un campo de estado al usuario creado
    data["status"] = "user created"
    return jsonify(data), 201

# Método PUT para actualizar datos de un usuario existente
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    # Se simula la actualización de datos de usuario
    data = request.get_json()
    # Actualización de los datos del usuario con el ID especificado
    # data contiene los nuevos datos para actualizar
    updated_user = {
        "id": user_id,
        "nombre": data.get("nombre", "test"),
        "codigo estudiantil": data.get("codigo estudiantil", "999.888.777"),
        "status": "user updated"  # Agregando un campo de estado para mostrar que el usuario fue actualizado
    }
    return jsonify(updated_user), 200

# Método DELETE para eliminar un usuario
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Se simula la eliminación
    deleted_user = {"id": user_id, "status": "user deleted"}
    return jsonify(deleted_user), 200

if __name__ == "__main__":
    app.run(debug=True)
