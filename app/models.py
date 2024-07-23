from . import db

class URL(db.Model):
    print('Clase url')
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(8), unique=True, nullable=False)
