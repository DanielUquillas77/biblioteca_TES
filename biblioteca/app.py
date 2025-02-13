# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_restful import Api, Resource, reqparse
from models import db, Book
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos con la aplicación
db.init_app(app)

# Crear la API RESTful
api = Api(app)

# Crear las tablas en la base de datos antes de la primera solicitud
#@app.before_first_request
#def create_tables():
#    db.create_all()
with app.app_context():
    db.create_all()
    
# ========================
# RUTAS WEB (INTERFAZ)
# ========================

# Página de listado y búsqueda de libros
@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('q', '')
    if search_query:
        books = Book.query.filter(
            (Book.title.ilike(f"%{search_query}%")) |
            (Book.author.ilike(f"%{search_query}%")) |
            (Book.genre.ilike(f"%{search_query}%"))
        ).all()
    else:
        books = Book.query.all()
    return render_template('index.html', books=books, search_query=search_query)

# Página para agregar un nuevo libro
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']
        new_book = Book(title=title, author=author, genre=genre, year=year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html')

# Página para editar un libro existente
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.year = request.form['year']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)

# Ruta para eliminar un libro
@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

# Ruta para eliminar múltiples libros
@app.route('/delete_multiple', methods=['POST'])
def delete_multiple():
    # Se obtienen los IDs de los libros seleccionados (lista de strings)
    selected_ids = request.form.getlist('selected_books')
    if selected_ids:
        # Convertir cada ID a entero y eliminar el libro correspondiente
        for book_id in selected_ids:
            book = Book.query.get(int(book_id))
            if book:
                db.session.delete(book)
        db.session.commit()
    return redirect(url_for('index'))
# ========================
# API RESTful
# ========================

# Recurso para listar y agregar libros vía API
class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return [book.to_dict() for book in books], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, help="El título es obligatorio")
        parser.add_argument('author', required=True, help="El autor es obligatorio")
        parser.add_argument('genre', required=True, help="El género es obligatorio")
        parser.add_argument('year', type=int, required=True, help="El año debe ser un número")
        args = parser.parse_args()

        new_book = Book(
            title=args['title'],
            author=args['author'],
            genre=args['genre'],
            year=args['year']
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book.to_dict(), 201

# Recurso para obtener, actualizar y eliminar un libro específico vía API
class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return book.to_dict(), 200

    def put(self, book_id):
        book = Book.query.get_or_404(book_id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, help="El título es obligatorio")
        parser.add_argument('author', required=True, help="El autor es obligatorio")
        parser.add_argument('genre', required=True, help="El género es obligatorio")
        parser.add_argument('year', type=int, required=True, help="El año debe ser un número")
        args = parser.parse_args()

        book.title = args['title']
        book.author = args['author']
        book.genre = args['genre']
        book.year = args['year']
        db.session.commit()
        return book.to_dict(), 200

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return '', 204

api.add_resource(BookListResource, '/api/books')
api.add_resource(BookResource, '/api/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
