from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
SECRET_HASH = environ.get('SECRET_HASH')

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer


db = SQLAlchemy()
mail = Mail()
s = URLSafeTimedSerializer(SECRET_HASH)
