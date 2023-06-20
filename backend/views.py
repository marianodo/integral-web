from flask import Blueprint, jsonify, request, url_for
from flask_cors import cross_origin
from flask_mail import Message
from itsdangerous import SignatureExpired, BadTimeSignature
from werkzeug.security import generate_password_hash

from extensions import db, mail, serializer
from models import WebUsers, Clients, Messages
from flask import current_app

main = Blueprint('main', __name__)

def send_token_to_email(email):
    current_app.logger.info('Creating Token')
    token = serializer.dumps(email, salt=email)
    msg = Message("Email de Confirmación", sender=current_app.config["MAIL_USERNAME"], recipients=[email])
    link = url_for("main.confirm_email", token=token, email=email, _external=True)
    msg.body = f"El link es: {link}"
    current_app.logger.info('Sending Email')
    mail.send(msg)

def add_update_web_user(email, password):
    current_app.logger.info("Adding/updating user")
    hash_password = generate_password_hash(password, method='sha256')

    user = WebUsers.query.filter_by(email=email).first()
    if not user: 
        new_user = WebUsers(email=email, password=hash_password)
        db.session.add(new_user)
    else:
        user.password = hash_password
        user.is_confirmed = False
    db.session.commit()


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
    print(current_app.config["MAIL_USERNAME"])
    user = Messages.query.first()
    print(user)
    return jsonify({"message": "hola"})

@main.route('/last_message/<client_id>', methods=['GET'])
def get_last_message(client_id):
    user = Messages.query.filter_by(cli_codigo=client_id).first()
    if not user:
        return f"No message for code {client_id}"

    last_message = {"code": user.cli_codigo, "message":user.men_contenido}
    last_message_str = f"code: {user.cli_codigo} message: {user.men_contenido}"
    msg = Message("Last Message", sender='integralcomweb@gmail.com', recipients=["mardom4164@gmail.com"])
    msg.body = f"Úlitmo Mensaje: {last_message_str}"
    mail.send(msg) 
    return jsonify(last_message)

import traceback

@main.route('/signup', methods=['POST'])
def register_new_user():
    # Get params
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        tb = traceback.format_exc()
        print(tb)
        print("AA")
        return tb

    add_update_web_user(email, password)
    send_token_to_email(email)

    return f"Token sent to {email}"

@main.route("/confirm_email/<token>/<email>")
def confirm_email(token, email):
    try:
        serializer.loads(token, salt = email, max_age=60)
    except SignatureExpired:
        return "The token is expired"
    except BadTimeSignature:
        return "Bad Token"
    
    user = WebUsers.query.filter_by(email=email).first()
    user.is_confirmed = True
    db.session.commit()
    return "The token works"