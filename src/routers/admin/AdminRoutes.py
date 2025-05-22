from flask import Blueprint, request, redirect, url_for, render_template, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mysqldb import MySQL

# Models
from models.ModelUser import ModelUser
from models import ModelApi
from models.crud_models import RecluseModels

# Entities
from models.entities.User import User

class AdminRoutes:
    def __init__(self, db):
        self.Admin = Blueprint('AdminRoutes', __name__, template_folder="templates")
        self.config_routes()
        self.db = db
        
    def config_routes(self):
        @self.Admin.route('/admin/register-recluses', methods=['GET', 'POST'])
        @login_required
        def insert_recluses():
            if current_user.type_usr == 'A':
                if request.method == 'POST':
                    data = request.form.to_dict()
                    archivo = request.files.get('Datos_personales')

                    if archivo and archivo.filename:
                        print(archivo.filename)
                    else:
                        print("No se subió ningún archivo.")

                    row = RecluseModels.Recluses.Create(self.db, data)
                    print(data)
                    if row is not None:
                        return redirect(url_for('home_admin'))
                    else:
                        flash("Hubo un error")
                return render_template('admin/forms.html')
            return "<h1>Inautorizado</h1>"


        @self.Admin.route('/admin/register-recluses/edit/<int:id>', methods=['GET', 'POST'])
        @login_required
        def show_recluses(id):
            if current_user.type_usr == 'A':
                if request.method == 'GET':
                    data = request.form.to_dict()

                    row = RecluseModels.Recluses.show(self.db, id)

                    if row is not None:
                        return render_template('admin/edit_recluses.html', data=row)
                    else:
                        flash("Hubo un error")

                return redirect(url_for('home_admin'))
            
            return "<h1>Inautorizado</h1>"


        @self.Admin.route('/admin')
        @login_required
        def home_admin():
            reclusos = ModelApi.Apis.recluseApi(self.db)

            if current_user.type_usr != 'A':
                return jsonify({'Access': 'Deny'})
            
            return render_template('admin/index.html', data=reclusos)
