from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

bookList = [
    {'id': 1, 'genre': 'Fiction', 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee',
     'year': 2007, 'publisher': 'J.B. Lippincott & Co.'},
    {'id': 2, 'genre': 'Fiction', 'title': 'Sapiens: A Brief History of Humankind', 'author':
     'Yuval Noah Harari', 'year': 2014, 'publisher': 'Harper'},
    {'id': 3, 'genre': 'Fiction', 'title': '1984', 'author': 'George Orwell', 'year': 2000,
     'publisher': 'Secker & Warburg'}
]

def get_next_id():
    if not bookList:
        return 1
    return max(book['id'] for book in bookList) + 1

@app.route('/')
def index():
    return render_template('index.html', bookList=bookList)

@app.route('/submit_action', methods=['POST'])
def submit_action():
    action = request.form.get('action')
    
    if action == 'create':
        return render_template('index.html', bookList=bookList, show_create_modal=True)
    
    elif action == 'update':
        selected_ids = request.form.getlist('selected_ids')
        if not selected_ids:
            return render_template('index.html', bookList=bookList, error='Please select a book to update')
        if len(selected_ids) > 1:
            return render_template('index.html', bookList=bookList, error='Please select only one book to update')
        
        book_id = int(selected_ids[0])
        book = next((b for b in bookList if b['id'] == book_id), None)
        return render_template('index.html', bookList=bookList, show_update_modal=True, selected_book=book)
    
    elif action == 'delete':
        selected_ids = request.form.getlist('selected_ids')
        if not selected_ids:
            return render_template('index.html', bookList=bookList, error='Please select book(s) to delete')
        
        for book_id in selected_ids:
            bookList[:] = [b for b in bookList if b['id'] != int(book_id)]
        
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/create_book', methods=['POST'])
def create_book():
    new_book = {
        'id': get_next_id(),
        'genre': request.form.get('genre'),
        'title': request.form.get('title'),
        'author': request.form.get('author'),
        'year': int(request.form.get('year')),
        'publisher': request.form.get('publisher')
    }
    bookList.append(new_book)
    return redirect(url_for('index'))

@app.route('/update_book', methods=['POST'])
def update_book():
    book_id = int(request.form.get('book_id'))
    for book in bookList:
        if book['id'] == book_id:
            book['genre'] = request.form.get('genre')
            book['title'] = request.form.get('title')
            book['author'] = request.form.get('author')
            book['year'] = int(request.form.get('year'))
            book['publisher'] = request.form.get('publisher')
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)