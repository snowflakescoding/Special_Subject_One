from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  

DATABASE = 'books.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            publisher TEXT NOT NULL
        )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM book')
    if cursor.fetchone()[0] == 0:
        sample_books = [
            ('Fiction', 'To Kill a Mockingbird', 'Harper Lee', 2007, 'J.B. Lippincott & Co.'),
            ('Fiction', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 2014, 'Harper'),
            ('Fiction', '1984', 'George Orwell', 2000, 'Secker & Warburg')
        ]
        cursor.executemany(
            'INSERT INTO book (genre, title, author, year, publisher) VALUES (?, ?, ?, ?, ?)',
            sample_books
        )
    
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM book ORDER BY id').fetchall()
    conn.close()
    return render_template('index.html', bookList=books)

@app.route('/submit_action', methods=['POST'])
def submit_action():
    action = request.form.get('action')
    
    if action == 'create':
        conn = get_db_connection()
        books = conn.execute('SELECT * FROM book ORDER BY id').fetchall()
        conn.close()
        return render_template('index.html', bookList=books, show_create_modal=True)
    
    elif action == 'update':
        selected_ids = request.form.getlist('selected_ids')
        if not selected_ids:
            conn = get_db_connection()
            books = conn.execute('SELECT * FROM book ORDER BY id').fetchall()
            conn.close()
            return render_template('index.html', bookList=books, error='Please select a book to update')
        if len(selected_ids) > 1:
            conn = get_db_connection()
            books = conn.execute('SELECT * FROM book ORDER BY id').fetchall()
            conn.close()
            return render_template('index.html', bookList=books, error='Please select only one book to update')
        
        book_id = int(selected_ids[0])
        conn = get_db_connection()
        book = conn.execute('SELECT * FROM book WHERE id = ?', (book_id,)).fetchone()
        books = conn.execute('SELECT * FROM book ORDER BY id').fetchall()
        conn.close()
        return render_template('index.html', bookList=books, show_update_modal=True, selected_book=book)
    
    elif action == 'delete':
        selected_ids = request.form.getlist('selected_ids')
        if not selected_ids:
            conn = get_db_connection()
            books = conn.execute('SELECT * FROM book ORDER BY id').fetchall()
            conn.close()
            return render_template('index.html', bookList=books, error='Please select book(s) to delete')
        
        conn = get_db_connection()
        for book_id in selected_ids:
            conn.execute('DELETE FROM book WHERE id = ?', (int(book_id),))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/create_book', methods=['POST'])
def create_book():
    genre = request.form.get('genre')
    title = request.form.get('title')
    author = request.form.get('author')
    year = int(request.form.get('year'))
    publisher = request.form.get('publisher')
    
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO book (genre, title, author, year, publisher) VALUES (?, ?, ?, ?, ?)',
        (genre, title, author, year, publisher)
    )
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/update_book', methods=['POST'])
def update_book():
    book_id = int(request.form.get('book_id'))
    genre = request.form.get('genre')
    title = request.form.get('title')
    author = request.form.get('author')
    year = int(request.form.get('year'))
    publisher = request.form.get('publisher')
    
    conn = get_db_connection()
    conn.execute(
        'UPDATE book SET genre = ?, title = ?, author = ?, year = ?, publisher = ? WHERE id = ?',
        (genre, title, author, year, publisher, book_id)
    )
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/api/list', methods=['GET'])
def api_list():
    try:
        conn = get_db_connection()
        books = conn.execute('SELECT * FROM book ORDER BY id').fetchall()
        conn.close()
        
        books_list = []
        for book in books:
            books_list.append({
                'id': book['id'],
                'genre': book['genre'],
                'title': book['title'],
                'author': book['author'],
                'year': book['year'],
                'publisher': book['publisher']
            })
        
        return jsonify(books_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/add', methods=['POST'])
def api_add():
    try:
        data = request.get_json()
        
        required_fields = ['genre', 'title', 'author', 'year', 'publisher']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        conn = get_db_connection()
        cursor = conn.execute(
            'INSERT INTO book (genre, title, author, year, publisher) VALUES (?, ?, ?, ?, ?)',
            (data['genre'], data['title'], data['author'], int(data['year']), data['publisher'])
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'message': 'Book added successfully',
            'id': new_id
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/update', methods=['POST'])
def api_update():
    try:
        book_id = request.args.get('id')
        if not book_id:
            return jsonify({'error': 'Book ID is required'}), 400
        
        data = request.get_json()
        
        required_fields = ['genre', 'title', 'author', 'year', 'publisher']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        conn = get_db_connection()
        
        book = conn.execute('SELECT * FROM book WHERE id = ?', (int(book_id),)).fetchone()
        if not book:
            conn.close()
            return jsonify({'error': 'Book not found'}), 404
        
        conn.execute(
            'UPDATE book SET genre = ?, title = ?, author = ?, year = ?, publisher = ? WHERE id = ?',
            (data['genre'], data['title'], data['author'], int(data['year']), data['publisher'], int(book_id))
        )
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Book updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/delete', methods=['GET'])
def api_delete():
    try:
        book_id = request.args.get('id')
        if not book_id:
            return jsonify({'error': 'Book ID is required'}), 400
        
        conn = get_db_connection()
        
        book = conn.execute('SELECT * FROM book WHERE id = ?', (int(book_id),)).fetchone()
        if not book:
            conn.close()
            return jsonify({'error': 'Book not found'}), 404
        
        conn.execute('DELETE FROM book WHERE id = ?', (int(book_id),))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Book deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)