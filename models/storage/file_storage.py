#!/usr/bin/python3
"""This is the file storage class for LIBRARIFY"""
import json
from models.librarify_base import LibrarifyBase
from models.user import User
from models.book import Book
from models.book_review import Review
import shlex


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'librarify.json'
    __objects = {}
    class_dict = {"LibrarifyBase":LibrarifyBase, "User":User,
                    "Book":Book, "Review":Review}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        '''Add new obj to existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''Save obj dictionaries to json file'''
        serialized_dict = {}

        for key, value in self.__objects.items():
            serialized_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_dict, f)

    def reload(self):
        '''If json file exists,
        convert obj dicts back to instances'''
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]