import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Cấu hình Database
# LƯU Ý: Khi chạy local, bạn có thể dùng SQLite. 
# Khi lên Vercel, biến môi trường DATABASE_URL sẽ được tự động cung cấp.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL') or 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODEL (Cấu trúc dữ liệu) ---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Tạo bảng database (chỉ chạy khi cần thiết, tốt nhất nên dùng migration sau này)
with app.app_context():
    db.create_all()

# --- ROUTES (Chức năng) ---

# 1. Xem danh sách (READ)
@app.route('/')
def index():
    # Lấy tasks chưa hoàn thành trước, rồi đến đã hoàn thành
    tasks = Task.query.order_by(Task.is_completed, Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

# 2. Thêm Task (CREATE)
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

# 3. Chỉnh sửa Task (UPDATE - View & Save)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

# 3.1 Cập nhật trạng thái Hoàn thành nhanh (UPDATE)
@app.route('/toggle/<int:id>')
def toggle_task(id):
    task = Task.query.get_or_404(id)
    task.is_completed = not task.is_completed
    db.session.commit()
    return redirect(url_for('index'))

# 4. Xóa Task (DELETE)
@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)