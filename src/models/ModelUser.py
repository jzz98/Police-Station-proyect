from .entities.User import User, Admin
from werkzeug.security import generate_password_hash
from flask_login import current_user
class ModelUser():
    @classmethod
    def login(cls, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT ID, username, password_user, Email, fullname, Type_usr FROM Users WHERE username = %s"""
            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()
            print(row)
            if row is not None:
                id, username, hashed_password, email,fullname, type_usr = row

                # Verificar contraseña usando el método del User
                if User.check_password(hashed_password, user.password):
                    if type_usr == 'A':
                        return Admin(id, username, hashed_password, email,fullname, type_usr)
                    else:
                        return User(id, username, hashed_password, email, fullname, type_usr)
                else:
                    return None  
            else:
                return None  # Usuario no encontrado

        except Exception as exp:
            raise Exception(exp)


    @classmethod
    def register(cls, db, user):
        try:
            cursor = db.connection.cursor()

            hashed_password = generate_password_hash(user.password)
            sql1 = """SELECT * FROM Users WHERE username = %s"""
            
            user_logged = cursor.execute(sql1, (user.username, ))

            if user_logged > 0:
                return False
            
            sql2 = """INSERT INTO Users (username, password_user, fullname, Email, Type_usr) 
                     VALUES (%s, %s, %s, %s, %s)"""

            cursor.execute(sql2, (user.username, hashed_password, user.fullname, user.email,'U'))
            db.connection.commit()

            return True 
        except Exception as exp:
            raise Exception(exp)


    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT ID, username, type_usr, fullname FROM Users WHERE ID = %s"""
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            
            if row is not None:
                if row[2] == 'A':
                    return Admin(row[0], row[1], None, row[3], row[2])
                return User(row[0], row[1], None, row[3], row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
