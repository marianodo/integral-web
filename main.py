from flask import Flask
from flask import jsonify

from config import config

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route('/api/v1/get_messages', methods=['GET'])
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

@app.route('/', methods=['GET'])
def get_main():
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')