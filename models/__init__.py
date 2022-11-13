#!/usr/bin/python3
'''
 Creating a unique FileStorage
 instance for the application
'''
from models.storage.file_storage import FileStorage

storage = FileStorage()
storage.reload()