class Config():
    SECRET_KEY = 'Hola'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'Estacion_policial'    

config = {
    'development': DevelopmentConfig
}