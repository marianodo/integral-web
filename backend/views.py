import traceback
from flask_login import login_user, current_user, login_required, logout_user
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_cors import cross_origin
from flask_mail import Message
from itsdangerous import SignatureExpired, BadTimeSignature
from werkzeug.security import generate_password_hash, check_password_hash

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


@main.route('/', methods=['GET'])
@login_required
def index():
    if not current_user.is_authenticated:
         return redirect(url_for('main.login'))
    
    email = current_user.email
    clients = Clients.query.filter(Clients.cli_mail.like(email)).all()
    codes = [c.cli_codigo for c in clients]
    messages = Messages.query.filter(Messages.cli_codigo.in_(codes)).order_by(Messages.men_fecha.desc()).all()
    if not messages:
        return f"No message for code {4220}"

    last_messages = [{"code": m.cli_codigo, "message":m.men_contenido, "date":f"{m.men_fecha} {m.men_hora}"} for m in messages]
    return render_template('index.html', messages=last_messages, name = email)

@main.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    remember = True if request.form.get('remember') else False

    user = WebUsers.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Usuario o contraseña incorrecte. Verifique')
        return redirect(url_for('main.login')) # if the user doesn't exist or password is wrong, reload the page
    
    print(user.is_confirmed)
    if not user.is_confirmed:
        flash('Cuenta no verificada. Por favor valide el token nuevamente')
        return redirect(url_for('main.signup')) # if the user doesn't exist or password is wrong, reload the page
    
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))

    

@main.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@main.route('/signup', methods=['POST'])
def register_new_user():
    # Get params
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        tb = traceback.format_exc()
        return tb

    add_update_web_user(email, password)
    send_token_to_email(email)

    return redirect(url_for('main.login'))

@main.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


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