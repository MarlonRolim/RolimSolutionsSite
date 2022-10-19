import os, random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET = 'aaaa'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:marlon123321@localhost:3306/curso_flask'


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'  # Aqui	geralmente	é	um	IP	de	um	servidor	na	nuvem	e	não	o	endereço	da	máquina	local
    PORT_HOST = 5000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:marlon123321@localhost:3306/curso_flask'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost'  # Aqui	geralmente	é	um	IP	de	um	servidor	na	nuvem	e	não	o	endereço	da	máquina	local
    PORT_HOST = 8080
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:marlon123321@localhost:3306/curso_flask'


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active ='development'
#os.getenv('FLASK_ENV')
if app_config is None:
    app_config = 'development'