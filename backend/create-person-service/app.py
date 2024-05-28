from flask import Flask, request, jsonify, make_response
from os import environ
from models import db
from models.user import User
from models.log import Log

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db.init_app(app)


@app.route('/create-user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(
            tipo=data['tipo'],
            numdoc=data['numdoc'],
            nombre=data['nombre'],
            segundo_nombre=data.get('segundo_nombre'),
            apellidos=data['apellidos'],
            f_nacimiento=data['f_nacimiento'],
            genero=data['genero'],
            correo=data['correo'],
            celular=data['celular'],
            foto=data['foto'].encode('utf-8') if data.get('foto') else None
        )
        db.session.add(new_user)
        db.session.commit()
        log_entry = Log(tipo='CREATE', document=new_user.numdoc)
        db.session.add(log_entry)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user', 'error': str(e)}), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
