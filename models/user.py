#!/usr/bin/python3
"""
User creation class
"""
from models.librarify_base import LibrarifyBase


class User(LibrarifyBase):
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    user_name = ""
    country = ""
    mail_address = ""