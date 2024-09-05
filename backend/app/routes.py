from flask import Blueprint, jsonify, request
from .models import db, User, Book
from .services.auth_service import create_user, verify_user
from .services.book_service import add_book, get_books

main = Blueprint('main', __name__)

@main.route('/api/register', methods=['POST'])
def register():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': 'User registered successfully!'})

@main.route('/api/login', methods=['POST'])
def login():
    data = request.json
    access_token = verify_user(data['username'], data['password'])
    if access_token:
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@main.route('/api/users/<int:id>/books', methods=['POST'])
def add_user_book(id):
    data = request.json
    add_book(id, data['title'], data['author'])
    return jsonify({'message': 'Book added successfully!'})

@main.route('/api/users/<int:id>/books', methods=['GET'])
def list_user_books(id):
    books = get_books(id)
    return jsonify([{'title': book.title, 'author': book.author} for book in books])

