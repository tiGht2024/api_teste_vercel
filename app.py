from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)

@app.route('/jwt/<string:id>', methods=['POST'])
def make_jwt(id):
    # Chave secreta para codificar e decodificar o token
    SECRET_KEY = 'fbed8ea0-6a5c-4ad1-a9ef-a8b5a463e0ab'

    # Dados a serem codificados no token
    payload = {
        'user_id': str(id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  
    }

    # Gerar o token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return jsonify({"token": token}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)