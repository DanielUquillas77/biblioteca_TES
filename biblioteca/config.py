# config.py
class Config:
    # Conexión a una base de datos SQLite (se crea el archivo library.db en el directorio)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
