from pathlib import Path
from os import path, getenv
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

root_path = Path(__file__).parent.parent
load_dotenv(path.join(root_path, '.env'))
SECRET_HASH = getenv('SECRET_HASH')

db = SQLAlchemy()
mail = Mail()
serializer = URLSafeTimedSerializer(SECRET_HASH)
