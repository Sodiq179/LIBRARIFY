#!/usr/bin/python3
'''
 Creating a unique FileStorage
 instance for the application
'''
from models.storage.file_storage import FileStorage
from models.storage.db_storage import DBStorage
from os import getenv
from models.librarify_base import LibrarifyBase
from models.user import User
from models.book import Book
from models.book_review import Review


if getenv("LIBRARIFY_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
