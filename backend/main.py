from views import main
from extensions import db, mail
from flask import Flask
from flask_login import LoginManager

from config import config

from flask import Flask
from flask_cors import CORS

def create_app(enviroment):
    app = Flask(__name__)
    CORS(app)
    
    app.config.from_object(enviroment)
    app.secret_key = 'super secret key'
    app.register_blueprint(main)

    # Initi DB
    db.init_app(app)
    mail.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    from models import WebUsers

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return WebUsers.query.get(int(user_id))
    

    return app

enviroment = config['development']
app = create_app(enviroment)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')