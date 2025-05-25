from flask import Blueprint, request, redirect, url_for, render_template, flash, jsonify, make_response
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mysqldb import MySQL
import os
# middlewares
from middlewares.auth.token import Token
# Models
from models.ModelUser import ModelUser
from models import ModelApi
from models.crud_models import RecluseModels

# Entities
from models.entities.User import User

# Controllers
from controllers.auth.register import RegisterController

class MainRoutes:
    def __init__(self, db):
        self.token = Token()
        self.MainRoutes = Blueprint('MainRoutes', __name__, template_folder="templates")
        self.config_routes()
        self.db = db

    def config_routes(self):
        @self.MainRoutes.route('/')
        def _ ():
            return redirect('home')
        
        @self.MainRoutes.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == "POST":
                username = request.form.get('username')
                password = request.form.get('password')
                
                result = RegisterController.login(self.token, username, password, self.db)
                return result
            
            return render_template('auth/login.html')


        @self.MainRoutes.route('/register', methods=['GET', 'POST'])
        def register():
            if request.method == 'POST':
                username = request.form.get('username')
                password = request.form.get('password')
                fullname = request.form.get('fullname')
                email = request.form.get('email')

                user = RegisterController.register(username, password, email, fullname, self.db)
                if user:
                    return redirect('/home')
                    # pass
                else:
                    print('Usuario registradp1')
                    flash('Usuario registrado')
                    return render_template('auth/register.html')

            else:
                return render_template('auth/register.html')
        
        @self.MainRoutes.route('/home')
        def homepage():
            return render_template('common/homepage.html')

            # token = request.cookies.get('token')  # <-- desde cookie
            # if not token:
            #     return jsonify({"message": "Token missing"}), 401

            # valid = self.token.validate_token(token, output=True)
            # if request.method == ''
            #     return render_template('common/homepage.html')
            # else:
            #     return valid  # respuesta de error desde validate_token
        
                
        @self.MainRoutes.route('/logout')
        def logout():
            logout_user()
            response = make_response(redirect(url_for('MainRoutes.login')))  # Cambiado a 'MainRoutes.login'
            response.delete_cookie('token')  # Eliminar la cookie JWT
            return response