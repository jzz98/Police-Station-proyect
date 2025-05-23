from flask_login import login_user
from flask import make_response, redirect,flash
# Models
from models.ModelUser import ModelUser
from models import ModelApi
from models.crud_models import RecluseModels

# middlewares
from middlewares.auth.token import Token

# Entities
from models.entities.User import User

class RegisterController:
    @staticmethod
    def register(username, password, email, fullname, db):
        user = User(0, username, password, email, fullname, )
        
        try:
            ModelUser.register(db, user)
            return True
        except Exception as exp:
            print(f"Error al registrar usuario: {exp}")
            return False
            

    @staticmethod
    def login(token, username, password, db):
        data = {
            "username": username,
            "password": password
        }

        # Verificar usuario desde la base de datos
        user = User(0, username, password)
        logged_user = ModelUser.login(db, user)

        if logged_user:
            login_user(logged_user)

            # Generar token
            token = token.write_token(data=data)

            # Preparar respuesta y agregar cookie con el token
            response = make_response(redirect('/admin' if logged_user.__class__.__name__ == 'Admin' else '/home'))
            response.set_cookie('token', token, httponly=True)
            return response

        flash('Usuario o contraseña incorrectos')
        return redirect('/login')
