from flask import Flask

def criarAPI():
    # Inicializando Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '0000'

    # Registrando Blueprint
    from .rotasR import rotasR
    app.register_blueprint(rotasR, url_prefix='/react')

    return app