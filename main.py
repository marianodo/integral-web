from views import main
from extensions import db
from flask import Flask
from config import config

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)
    app.register_blueprint(main)
    db.init_app(app)
    return app


enviroment = config['development']
app = create_app(enviroment)



# with app.app_context():
#     client = db.Table("cli_clientes", db.metadata, autoload=True, autoload_with=db.engine)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')