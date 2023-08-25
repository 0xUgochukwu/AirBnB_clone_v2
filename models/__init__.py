#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_type = getenv('HBNB_TYPE_STORAGE')
storage = DBStorage() if storage_type == 'db' else FileStorage()
storage.reload()
