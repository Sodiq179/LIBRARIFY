#!/usr/bin/python3
"""
User creation class
"""
from os import getenv
from models.librarify_base import LibrarifyBase, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(LibrarifyBase, Base):
    """Defines attributes for user creation"""
    __tablename__ = "users"
    if getenv("LIBRARIFY_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=True)
        password =  Column(String(128), nullable=True)
        first_name = Column(String(128), nullable=True)
        last_name =  Column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

