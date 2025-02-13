# models.py
from flask_sqlalchemy import SQLAlchemy

# Instancia de SQLAlchemy para la aplicación
db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)             # Identificador único
    title = db.Column(db.String(150), nullable=False)          # Título del libro
    author = db.Column(db.String(150), nullable=False)         # Autor del libro
    genre = db.Column(db.String(100), nullable=False)          # Género del libro
    year = db.Column(db.Integer, nullable=False)               # Año de publicación

    def to_dict(self):
        """Convierte el objeto Book a un diccionario para la API."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'year': self.year
        }
