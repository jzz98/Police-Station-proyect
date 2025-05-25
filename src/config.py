from os import getenv

class Config():
    SECRET_KEY = 'Hola'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = getenv('PASSWORD_DB')
    MYSQL_DB = getenv("DB_NAME")    

config = {
    'development': DevelopmentConfig
}