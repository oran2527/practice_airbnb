#!/usr/bin/python3
""" module point 1 base class """
import uuid
from datetime import datetime


class BaseModel:
    """class BaseModel"""


    def __init__(self, *args, **kwargs):
        """init function"""
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(value, "\
%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(value, "\
%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """str function"""
        return "[{}] ({}) {}\
".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """to_dict function"""
        n_dic = dict(self.__dict__)

        update = self.updated_at
        create = self.created_at

        n_dic["__class__"] = self.__class__.__name__
        n_dic["created_at"] = create.strftime("%Y-%m-%dT%H:%M:%S.%f")
        n_dic["updated_at"] = update.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return n_dic

    def save(self):
        """save function"""
        self.updated_at = datetime.datetime.now()
