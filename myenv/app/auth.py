from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para autenticar o usuário (simplificada para este exemplo)
def authenticate_user(username, password):
    if username == "admin" and password == "password":
        return True
    return False

# Endpoint para autenticar usuários
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if authenticate_user(username, password):
        # Aqui, você pode gerar e retornar um token JWT
        return jsonify({"message": "Login bem-sucedido"})
    else:
        return jsonify({"message": "Falha na autenticação"}), 401

if __name__ == '__main__':
    app.run(debug=True)
