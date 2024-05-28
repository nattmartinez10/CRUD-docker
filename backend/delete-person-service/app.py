from flask import Flask, request, jsonify, make_response
from os import environ
from models import db
from models.user import User
from models.log import Log
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db.init_app(app)

@app.route('/delete-user/<string:numdoc>', methods=['DELETE'])
def delete_user(numdoc):
    try:
        user = User.query.filter_by(numdoc=numdoc).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            log_entry = Log(tipo='DELETE', document=user.numdoc)
            db.session.add(log_entry)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting user', 'error': str(e)}), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

