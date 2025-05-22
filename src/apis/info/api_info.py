from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from models.ModelApi import Apis

class ApiReclusos:
    def __init__(self, db):
        self.api = Blueprint('info_api', __name__)
        self.db = db
        self.setup_routes()

    def setup_routes(self):
        @self.api.route('/api/v1/local/prt/information', methods=['GET'])
        def recluse():
            execute = Apis.recluseApi(self.db)

            if current_user != "A":
                return jsonify({'error': 'Unauthorized access'}), 403  # 403 Forbidden

            if execute:
                return jsonify(execute)
            else:
                return jsonify({'error': 'No data found'}), 404
