import os
from flask import request, flash
from flask_login import current_user
from werkzeug.utils import secure_filename

class Recluses:
    def __init__(self):
        user_folder = secure_filename(current_user.fullname)
        self.upload_folder = f'src/static/storage/user/{user_folder}'
        self.allow_extensions = {'png', 'jpg', 'pdf'}
        os.makedirs(self.upload_folder, exist_ok=True)

    def allowed_file(self, filename):
        return '.' in filename and filename.split('.', 1)[1].lower() in self.allow_extensions
    
    def upload_file(self):
        if 'Datos_biometricos' not in request.files or 'Datos_personales' not in request.files:
            flash('No se subieron los archivos')
            return None, None

        file1 = request.files['Datos_biometricos']
        file2 = request.files['Datos_personales']

        if file1.filename == '' or file2.filename == '':
            flash('Los datos no pueden estar vacíos')
            return None, None
        
        if not self.allowed_file(file1.filename) or not self.allowed_file(file2.filename):
            flash('Formato de archivo no permitido')
            return None, None

        return file1, file2
    
    @classmethod
    def Create(cls, db, data):
        try:
            instance = cls()
            print('datos', data)

            # file1, file2 = instance.upload_file()
            # if file1 is None or file2 is None:
            #     return False

            # # Sanitizar nombres de archivo
            # filename1 = file1.filename
            # filename2 = file2.filename

            # file1_path = os.path.join(instance.upload_folder, filename1)
            # file2_path = os.path.join(instance.upload_folder, filename2)

            cursor = db.connection.cursor()

            sql = """INSERT INTO Reclusos(
                Nombre, Apellido, ALias, Fecha_entrada, INT_Carcel, Numero_condenas, 
                Oficial_encargado, Estado) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(sql, (
                data.get('Nombre'),
                data.get('Apellido'),
                data.get('ALias'),
                data.get('Fecha_entrada'),
                data.get('INT_Carcel'),
                data.get('Numero_condenas'),
                data.get('Oficial_encargado'),
                data.get('Estado')
            ))
            
            db.connection.commit()
            # file1.save(file1_path)
            # file2.save(file2_path)
            
            flash('Archivos subidos con éxito')
            return True
            
        except Exception as exp:
            db.connection.rollback()
            flash(f'Error al procesar la solicitud: {str(exp)}')
            raise Exception(exp)  
              
    @classmethod
    def edit(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM Reclusos WHERE ID=%s"
            cursor.execute(sql, (id,))
            row =  cursor.fetchone()
            return row
        except Exception as exp:
            raise Exception(exp)
        
    def update(cls, id, db, data):
        try:
            cursor = db.connection.cursor()

            sql = """
                UPDATE Reclusos 
                SET Nombre, Apellido, ALias, Fecha_entrada, INT_Carcel, Numero_condenas, 
                Oficial_encargado, Estado WHERE ID = %s
                """
            valores = (
                data.get('Nombre'),
                data.get('Apellido'),
                data.get('ALias'),
                data.get('Fecha_entrada'),
                data.get('INT_Carcel'),
                data.get('Numero_condenas'),
                data.get('Oficial_encargado'),
                data.get('Estado'),
                id
            )

            cursor.execute(sql, valores)
            cursor.connection.commit()
            
            return True
        except Exception as exp:
            raise Exception(exp)
        