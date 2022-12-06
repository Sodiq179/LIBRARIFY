#!/usr/bin/python3
"""
Defines review class
"""
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.librarify_base import LibrarifyBase, Base


class Review(LibrarifyBase, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "reviews"
    if getenv("LIBRARIFY_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=True)
        book_id = Column(String(60), ForeignKey("books.id"), nullable=True)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=True)
    else:
        book_id = ""
        user_id = ""
        text = ""
