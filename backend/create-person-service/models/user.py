from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    numdoc = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50))
    segundo_nombre = db.Column(db.String(50), nullable=True)
    apellidos = db.Column(db.String(50))
    f_nacimiento = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    celular = db.Column(db.String(50))
    foto = db.Column(db.LargeBinary, nullable=True)

    def json(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'numdoc': self.numdoc,
            'nombre': self.nombre,
            'segundo_nombre': self.segundo_nombre,
            'apellidos': self.apellidos,
            'f_nacimiento': self.f_nacimiento,
            'genero': self.genero,
            'correo': self.correo,
            'celular': self.celular,
            'foto': self.foto.decode('latin1') if self.foto else None  # Decoding binary data for JSON serialization
        }

