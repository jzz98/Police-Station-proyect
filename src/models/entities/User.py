from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, email, fullname="", type_usr="U"):
        self.id = id
        self.username = username
        self.password = password  
        self.fullname = fullname
        self.email = email
        self.type_usr = type_usr

    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)

class Admin(User):
    def __init__(self, id, username, password, email, fullname, type_usr="A"):
        super().__init__(id, username, password, email, fullname, type_usr)
