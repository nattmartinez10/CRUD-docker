from flask import Flask, request, jsonify, make_response
from os import environ
from models import db
from models.log import Log
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db.init_app(app)


@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        tipo = request.args.get('tipo')
        document = request.args.get('document')
        date = request.args.get('date')

        query = Log.query
        if tipo:
            query = query.filter_by(tipo=tipo)
        if document:
            query = query.filter_by(document=document)
        if date:
            query = query.filter(Log.fecha_transaccion.like(f"{date}%"))

        logs = query.all()
        return make_response(jsonify([log.json() for log in logs]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting logs', 'error': str(e)}), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
