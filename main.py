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
    response = {'message': 'success'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')