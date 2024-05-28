from . import db

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    document = db.Column(db.String(50))
    fecha_transaccion = db.Column(db.DateTime, server_default=db.func.now())

    def json(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'document': self.document,
            'fecha_transaccion': self.fecha_transaccion
        }
