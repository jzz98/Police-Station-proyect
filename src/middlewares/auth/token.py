from jwt import encode, decode, exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify, request

class Token:
    @staticmethod
    def expired_time(days: int):
        now = datetime.now()
        return now + timedelta(days=days)

    def write_token(self, data: dict):
        token = encode(payload={**data, "exp": self.expired_time(2)}, key=getenv("SECRET"), algorithm="HS256")
        return token
    
    @staticmethod
    def validate_token(token, output=False):
        try:
            if output:
                return decode(token,  key=getenv("SECRET"), algorithms=["HS256"])
            decode(token,  key=getenv("SECRET"), algorithms=["HS256"])
        except exceptions.DecodeError:
            return jsonify({"message": "Invalid token"}), 401
        except exceptions.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401