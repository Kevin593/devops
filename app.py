from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
JWT_SECRET = "SuperSecretKeyForDevOps"
JWT_ALGORITHM = "HS256"

@app.route('/DevOps', methods=['POST', 'GET', 'PUT', 'DELETE'])
def devops():
    # Verificación de API Key
    api_key = request.headers.get('X-Parse-REST-API-Key')
    if api_key != API_KEY:
        return jsonify({"error": "Invalid API Key"}), 403

    # Solo aceptar POST
    if request.method != 'POST':
        return "ERROR", 400

    # Verificación de JWT
    jwt_token = request.headers.get('X-JWT-KWY')
    if not jwt_token:
        return jsonify({"error": "JWT missing"}), 403

    try:
        decoded = jwt.decode(jwt_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded.get("iat") is None:
            raise Exception("Invalid JWT")
    except Exception:
        return jsonify({"error": "Invalid JWT"}), 403

    # Validación del JSON recibido
    data = request.get_json()
    if not data or 'to' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    response = {
        "message": f"Hello {data['to']} your message will be send111"
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
