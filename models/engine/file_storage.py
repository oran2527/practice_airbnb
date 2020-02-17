#!/usr/bin/python3
""" module point 5 file_storage """
import json
import models
from models import *


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all function"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        objName = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[objName] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        n_dict = {}
        with open(self.__file_path, "w", encoding='utf-8') as f:
            for key, value in self.__objects.items():
                n_dict[key] = value.to_dict()
            json.dump(n_dict, f)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                o_dict = json.load(f)
                for key, value in o_dict.items():
                    cl = key.split(".")
                    value.pop("__class__")
                    if cl[0] == "BaseModel":
                        bmObj = BaseModel(**value)
                    if cl[0] == "User":
                        bmObj = User(**value)
                    if cl[0] == "State":
                        bmObj = State(**value)
                    if cl[0] == "City":
                        bmObj = City(**value)
                    if cl[0] == "Amenity":
                        bmObj = Amenity(**value)
                    if cl[0] == "Place":
                        bmObj = Place(**value)
                    if cl[0] == "Review":
                        bmObj = Review(**value)
                    self.new(bmObj)
        except:
            pass
