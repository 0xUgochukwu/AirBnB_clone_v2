#!/usr/bin/python3
""" Database Storage Module """
from os import getenv, environ
from operator import itemgetter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user, pwd, host, db = itemgetter(
                'HBNB_MYSQL_USER', 'HBNB_MYSQL_PWD',
                'HBNB_MYSQL_HOST', 'HBNB_MYSQL_DB')(environ)
        env = getenv('HBNB_ENV')
        db_url = f"mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == "test":
            Base.metaData.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}

        if cls is None:
            classes = [City, State]
            for _cls in classes:
                for obj in self.__session.query(_cls).all():
                    objects[f"{_cls}.{obj.id}"] = obj
        else:
            for obj in self.__session.query(cls).all():
                objects[f"{cls}.{obj.id}"] = obj
        return objects

    def new(self, obj):
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()
