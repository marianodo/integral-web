from flask_login import UserMixin
from extensions import db
from werkzeug.security import check_password_hash, generate_password_hash
class WebUsers(UserMixin, db.Model):
    __tablename__ = "web_users"

    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String)
    password = db.Column("password", db.String)
    is_confirmed = db.Column("is_confirmed", db.Boolean, default=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f"{self.email}"


class Clients(db.Model):
    __tablename__ = "cli_clientes"

    cli_id = db.Column("cli_id", db.Integer, primary_key=True)
    civa_id = db.Column("civa_id", db.Integer)
    bar_id = db.Column("bar_id", db.Integer)
    cli_codigo = db.Column("cli_codigo", db.Integer)
    cli_razon_social = db.Column("cli_razon_social", db.String)
    cli_nombre_fantasia = db.Column("cli_nombre_fantasia", db.String)
    cli_cuit = db.Column("cli_cuit", db.String)
    cli_contacto = db.Column("cli_contacto", db.String)
    cli_calle = db.Column("cli_calle", db.String)
    cli_nro = db.Column("cli_nro", db.String)
    cli_piso = db.Column("cli_piso", db.String)
    cli_dpto = db.Column("cli_dpto", db.String)
    cli_codigo_postal = db.Column("cli_codigo_postal", db.String)
    cli_telefono = db.Column("cli_telefono", db.String)
    cli_codigo_postal = db.Column("cli_codigo_postal", db.String)
    cli_telefono = db.Column("cli_telefono", db.String)
    cli_celular = db.Column("cli_celular", db.String)
    cli_mail = db.Column("cli_mail", db.String)
    cli_observaciones = db.Column("cli_observaciones", db.String)
    cli_destino = db.Column("cli_destino", db.String)
    cli_mail_administrativo = db.Column("cli_mail_administrativo", db.String)
    cli_estado = db.Column("cli_estado", db.String)
    cli_asociado = db.Column("cli_asociado", db.Integer)
    cli_habilita_asociado = db.Column("cli_habilita_asociado", db.String)

    def __repr__(self) -> str:
        return f"{self.cli_codigo}"

class Messages(db.Model):
    __tablename__ = "men_mensajes"
    
    men_id = db.Column("men_id", db.Integer, primary_key=True)
    cli_codigo = db.Column("cli_codigo", db.Integer)
    men_fecha = db.Column("men_fecha", db.Date)
    men_hora = db.Column("men_hora", db.String)
    men_contenido = db.Column("men_contenido", db.String)
    men_mail = db.Column("men_mail", db.String)
    men_beeper = db.Column("men_beeper", db.String)
    men_celular = db.Column("men_celular", db.String)
    men_enviar_x_beeper = db.Column("men_enviar_x_beeper", db.Integer)
    men_enviar_x_mail = db.Column("men_enviar_x_mail", db.Integer)
    men_enviar_x_celular = db.Column("men_enviar_x_celular", db.Integer)
    men_destino = db.Column("men_destino", db.String)
    men_cargado_en_web = db.Column("men_cargado_en_web", db.String)
    men_origen = db.Column("men_origen", db.String)
    men_operador = db.Column("men_operador", db.String)
    men_estado = db.Column("men_estado", db.String)
    men_origen_id = db.Column("men_origen_id", db.Integer)
    men_original = db.Column("men_original", db.Integer)

    def __repr__(self) -> str:
        return f"Code: {self.cli_codigo}, Message: {self.men_contenido}"