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

@app.route('/update-user/<string:numdoc>', methods=['PUT'])
def update_user(numdoc):
    try:
        user = User.query.filter_by(numdoc=numdoc).first()
        if user:
            data = request.get_json()
            if not data:
                return make_response(jsonify({'message': 'No input data provided'}), 400)

            user.tipo = data.get('tipo', user.tipo)
            user.numdoc = data.get('numdoc', user.numdoc)
            user.nombre = data.get('nombre', user.nombre)
            user.segundo_nombre = data.get('segundo_nombre', user.segundo_nombre)
            user.apellidos = data.get('apellidos', user.apellidos)
            user.f_nacimiento = data.get('f_nacimiento', user.f_nacimiento)
            user.genero = data.get('genero', user.genero)
            user.correo = data.get('correo', user.correo)
            user.celular = data.get('celular', user.celular)
            
            # Handle foto field
            if 'foto' in data and data['foto']:
                user.foto = data['foto'].encode('utf-8')  # Ensure foto is correctly encoded

            db.session.commit()

            log_entry = Log(tipo='UPDATE', document=user.numdoc)
            db.session.add(log_entry)
            db.session.commit()

            return make_response(jsonify({'message': 'User updated', 'user': user.json()}), 200)

        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        db.session.rollback()
        app.logger.error(f'Error updating user: {str(e)}')  # Log the error
        return make_response(jsonify({'message': 'Error updating user', 'error': str(e)}), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

