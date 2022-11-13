#!/usr/bin/python3
"""
Defines review class
"""
from models.librarify_base import LibrarifyBase


class Review(LibrarifyBase):
    """Reviews made by users about a book"""
    book_id = ""
    user_id = ""
    text = ""
    rating = 0
    liked = ""