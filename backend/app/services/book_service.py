from app.models import db, Book

def add_book(user_id, title, author):
    new_book = Book(title=title, author=author, user_id=user_id)
    db.session.add(new_book)
    db.session.commit()

def get_books(user_id):
    return Book.query.filter_by(user_id=user_id).all()
