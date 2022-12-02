#!/usr/bin/python3
"""
User creation class
"""
from models.librarify_base import LibrarifyBase, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import shlex
from os import getenv


class Book(LibrarifyBase, Base):
    """Defines attributes for user creation"""
    __tablename__ = "books"
    if getenv("LIBRARIFY_TYPE_STORAGE") == "db":
        author = Column(String(128), nullable=True)
        title = Column(String(128), nullable=True)
        category = Column(String(128))
        publication_year = Column(Integer, nullable=True)
        image_url = Column(String(128), nullable=True)
        book_api  = Column(String(128), nullable=True)
        publisher = Column(String(128), nullable=True)

    else:
        author=""
        title=""
        category=""
        publication_year=0
        image_url=""
        book_api=""
        publisher=""
