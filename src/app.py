from flask import Flask, redirect, url_for, render_template, request, flash, jsonify, abort
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from  werkzeug.routing import BuildError

# Apis
from apis.info.api_info import ApiReclusos
# Configuración
from config import config

# Models
from models.ModelUser import ModelUser
from models import ModelApi
from models.crud_models import RecluseModels

# Entities
from models.entities.User import User

# Routes
from routers.mainRoutes import MainRoutes
from routers.admin.AdminRoutes import AdminRoutes

class Server:
    def __init__(self):
        self.app = Flask(__name__, template_folder="templates")
        self.app.config.from_object(config['development'])

        self.db = MySQL(self.app)
        self.csrf = CSRFProtect(self.app)

        self.login_manager_app = LoginManager(self.app)
        self.login_manager_app.login_view = 'MainRoutes.login'  # Redirige si no está logueado

        self.configure_login()
        # self.routes()
        self.Error_handler()
        self.register_blueprints()
        self.login_manager_app.unauthorized_handler(self.custom_unauthorized)

    def custom_unauthorized(self):
        return redirect(url_for('MainRoutes.login'))
    
    def configure_login(self):
        @self.login_manager_app.user_loader
        def load_user(id):
            return ModelUser.get_by_id(self.db, id)
        
        @self.login_manager_app.unauthorized_handler
        def unauthorized():
            return redirect(url_for('MainRoutes.login'))
        
    def Error_handler(self):
        @self.app.errorhandler(404)
        def page_not_found(e):
            return redirect(url_for('MainRoutes.login'))
        
        @self.app.errorhandler(403)
        def page_not_found(e):
            return redirect(url_for('MainRoutes.login'))


    def register_blueprints(self):
        reclusos_api = ApiReclusos(self.db)
        RoutesMain = MainRoutes(self.db)
        RoutesAdmin = AdminRoutes(self.db)

        self.app.register_blueprint(reclusos_api.api)
        self.app.register_blueprint(RoutesMain.MainRoutes)
        self.app.register_blueprint(RoutesAdmin.Admin)
        
    def run(self):
        self.app.run(debug=True)
        # self.register_error_handler(401, self.status_401)
        self.config.from_object(config['development'])

if __name__ == '__main__':
    server = Server()
    load_dotenv()
    server.run()
