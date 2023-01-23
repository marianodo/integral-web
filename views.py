from flask import Blueprint
from flask import jsonify
from flask_cors import cross_origin

from extensions import db
from models import WebUsers, Clients, Messages

main = Blueprint('main', __name__)

@main.route('/api/v1/get_messages', methods=['GET'])
@cross_origin()
def get_users():
    response = [
        {"code": 4220, "date": "2023/01/10", "time": "20:20", "message": "Apertura de usuario"},
        {"code": 4220, "date": "2023/01/10", "time": "18:20", "message": "Cierre de usuario"},
        {"code": 4220, "date": "2023/01/09", "time": "20:20", "message": "Alarma habitación del dragon"},
        {"code": 1220, "date": "2023/01/10", "time": "14:20", "message": "Acuario en orden"},
        {"code": 4220, "date": "2023/01/08", "time": "15:10", "message": "Bau bauu"},
        {"code": 1220, "date": "2023/01/08", "time": "08:20", "message": "El acuario cerrado"},
        {"code": 1220, "date": "2023/01/07", "time": "09:20", "message": "Como está todo en el Acuario?"},
        {"code": 1220, "date": "2023/01/06", "time": "06:20", "message": "Acuario acá"}
        ]
    return jsonify(response)

@main.route('/', methods=['GET'])
def get_main():
    user = Messages.query.first()
    print(user)
    return jsonify({"message": "hola"})

@main.route('/last_message/<client_id>', methods=['GET'])
def get_last_message(client_id):
    user = Messages.query.filter_by(cli_codigo=client_id).first()
    if not user:
        return f"No message for code {client_id}"
        
    return jsonify({"code": user.cli_codigo, "message":user.men_contenido})