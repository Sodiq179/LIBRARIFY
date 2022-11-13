#!/usr/bin/python3
"""
User creation class
"""
from models.librarify_base import LibrarifyBase


class Book(LibrarifyBase):
    """Defines attributes for user creation"""
    author = ""
    title = ""
    category = ""
    publication_year = 0
    image_url = ""
    book_api  = ""
    publisher = ""