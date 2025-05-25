class Config():
    SECRET_KEY = 'Hola'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1v19514#'
    MYSQL_DB = 'Estacion_policial'    

config = {
    'development': DevelopmentConfig
}