from views import main
from extensions import db
from flask import Flask
from config import config

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)
    app.register_blueprint(main)

    # Initi DB
    db.init_app(app)
    return app

enviroment = config['development']
app = create_app(enviroment)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')