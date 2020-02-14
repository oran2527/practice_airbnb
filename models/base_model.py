#!/usr/bin/python3
""" module point 1 base class """
import uuid
import datetime


class BaseModel:
    """class BaseModel"""

    
    def __init__(self, my_number=0, name=""):
        """init function"""
        self.id = str(uuid.uuid4())
        self.my_number = my_number
        self.name = name
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """str function"""
        return "[{}] ({}) {}\
".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """to_dict function"""
        update = self.updated_at
        create = self.created_at

        return {'my_number': self.my_number, 'name': self.name, '__class__\
': self.__class__.__name__, 'updated_at\
': update.strftime("%Y-%m-%dT%H:%M:%S.%f"), 'id': self.id, 'created_at\
': create.strftime("%Y-%m-%dT%H:%M:%S.%f")}

    def save(self):
        """save function"""
        self.updated_at = datetime.datetime.now()
