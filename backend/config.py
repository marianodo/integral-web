from pathlib import Path
from os import environ, path, getenv
from dotenv import load_dotenv

root_path = Path(__file__).parent.parent
load_dotenv(path.join(root_path, '.env'))


SECRET_KEY = getenv('SECRET_KEY')
USER_DB = getenv('USER_DB')
HOST = getenv('HOST')
PORT = getenv('PORT')
DATABASE = getenv('DATABASE')
MAIL_SERVER = getenv('MAIL_SERVER')
MAIL_PORT = getenv('MAIL_PORT')
MAIL_USE_SSL = getenv('MAIL_USE_SSL')
MAIL_USE_TLS = getenv('MAIL_USE_TLS')
MAIL_USERNAME = getenv('MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD')
FLASK_SECRET_KEY = getenv('FLASK_SECRET_KEY')


class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = \
        f'mysql+mysqlconnector://{USER_DB}:{SECRET_KEY}@{HOST}:{PORT}/{DATABASE}?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'
    MAIL_SERVER = MAIL_SERVER
    MAIL_PORT = MAIL_PORT
    MAIL_USE_SSL = MAIL_USE_SSL
    MAIL_USE_TLS = MAIL_USE_TLS
    MAIL_USERNAME = MAIL_USERNAME
    MAIL_PASSWORD = MAIL_PASSWORD
    SECRET_KEY = FLASK_SECRET_KEY
config = {
    'development': DevelopmentConfig,
}