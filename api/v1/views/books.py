#!/usr/bin/python3
""" objects that handles all default RestFul API actions for Books"""
from models.book import Book
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/books', methods=['GET'], strict_slashes=False)
@swag_from('documentation/book/all_books.yml')
def get_books():
    """
    Retrieves a list of all books
    """
    all_books = storage.all(Book).values()
    list_books = []
    for book in all_books:
        list_books.append(book.to_dict())
    return jsonify(list_books)


@app_views.route('/books/<book_id>/', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/book/get_book.yml', methods=['GET'])
def get_book(book_id):
    """ Retrieves a book """
    book = storage.get(Book, book_id)
    if not book:
        abort(404)

    return jsonify(book.to_dict())


@app_views.route('/books/<book_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/book/delete_book.yml', methods=['DELETE'])
def delete_book(book_id):
    """
    Deletes a book  Object
    """

    book = storage.get(Book, book_id)

    if not book:
        abort(404)

    storage.delete(book)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/books', methods=['POST'], strict_slashes=False)
@swag_from('documentation/book/post_book.yml', methods=['POST'])
def post_book():
    """
    Creates a book
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Book(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/books/<book_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/book/put_book.yml', methods=['PUT'])
def put_book(book_id):
    """
    Updates a book
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    book = storage.get(Book, book_id)

    if not book:
        abort(404)

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(book, key, value)
    storage.save()
    return make_response(jsonify(book.to_dict()), 200)
