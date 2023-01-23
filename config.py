from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

SECRET_KEY = environ.get('SECRET_KEY')
USER_DB = environ.get('USER_DB')
HOST = environ.get('HOST')
PORT = environ.get('PORT')
DATABASE = environ.get('DATABASE')
class Config:
    pass
class DevelopmentConfig(Config):
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = \
        f'mysql+mysqlconnector://{USER_DB}:{SECRET_KEY}@{HOST}:{PORT}/{DATABASE}?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'

config = {
    'development': DevelopmentConfig,
}