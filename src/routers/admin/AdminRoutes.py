from flask import Blueprint, request, redirect, url_for, render_template, flash, jsonify, abort
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
            try:
                if current_user.type_usr == 'A':
                    if request.method == 'POST':
                        data = request.form.to_dict()
                        archivo = request.files.get('Datos_personales')

                        if archivo and archivo.filename:
                            pass
                        else:
                            print("No se subió ningún archivo.")

                        row = RecluseModels.Recluses.Create(self.db, data)

                        if row:
                            return redirect(url_for('AdminRoutes.home_admin'))
                        else:
                            flash("Hubo un error")
                            
                    return render_template('admin/forms.html')
                return "<h1>Inautorizado</h1>"
            except Exception as exp:
                raise Exception(exp)
            
        @self.Admin.route('/admin/register-recluses/edit/<int:id>', methods=['GET', 'POST'])
        @login_required
        def edit_recluses(id):
            if current_user.type_usr == 'A':
                if request.method == 'GET':
                    data = request.form.to_dict()

                    row = RecluseModels.Recluses.edit(self.db, id)

                    if row is not None:
                        return render_template('admin/edit_recluses.html', data=row)
                    else:
                        flash("Hubo un error")

                return redirect('/admin')
            
            return redirect('/login')
        
        @self.Admin.route('/admin/register-recluses/update/<int:id>', method=['GET', 'POST'])
        @login_required
        def update_recluses(id):
            if current_user.type_usr == 'A':
                if request.method == 'POST':
                    pass
        @self.Admin.route('/admin')
        @login_required
        def home_admin():
            if current_user.type_usr == 'A':
                reclusos = ModelApi.Apis.recluseApi(self.db)
                return render_template('admin/index.html', data=reclusos)

            return abort(403)