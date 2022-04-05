from flask import Flask, request, jsonify
from flask.helpers import make_response
import bancoDadosActions
app = Flask(__name__)

usuarios = {}

@app.route('/accounts/<id>', methods=['GET'])
def get_usuario(id):
    usuario = bancoDadosActions.obter_usuario(id)
    if(usuario):
        return jsonify({'id':usuario[0], 'email':usuario[3]})
    return jsonify({"status":'inexistente'}), 404

@app.route('/accounts', methods=['GET'])
def obter_usuarios():
    usuarios = bancoDadosActions.obter_usuarios()
    return jsonify({'usuarios':usuarios})

@app.route('/accounts', methods=['POST'])
def add__usuario():
    try:
        account = request.json
        usuario = bancoDadosActions.obter_usuario(account['user_id'])
        if (usuario):
            response = jsonify({"status": f"usuario {account['user_id']} existe"})
            response.status_code = 422
            return response
        
        bancoDadosActions.inserir_account(account)
        response = jsonify({'id':account['user_id'], 'email':account['email']})
        response.status_code = 201
        response.headers['location'] = f"/account/{account['user_id']}"
        print(response.headers)
        return response
    except Exception as e:
        print(e)
        raise

@app.route('/accounts/<id>', methods=['PUT'])
def replace_usuario(id):
    try:
        usuario = request.json
        usuario_bd = bancoDadosActions.obter_usuario(id)
        if usuario_bd:
            bancoDadosActions.modifica_conta(usuario)
            return '', 204 # no content response
        response = make_response(jsonify({'status': 'Not found'}), 404)
        return response
    except Exception as e:
        print(e)
        raise

@app.route('/accounts/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario_bd = bancoDadosActions.obter_usuario(id)
        if usuario_bd:
            bancoDadosActions.deletar_conta(id)
            return '', 204 # no content response
        return make_response(jsonify({'status': 'Not found'}), 404)
    except Exception as e:
        print(e)
        raise

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=8080)
