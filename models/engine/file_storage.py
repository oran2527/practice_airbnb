#!/usr/bin/python3
""" module point 5 file_storage """


class FileStorage:
    """class FileStorage"""

    def __init__(self):
        """init function""" 
        self.__file__path = "file.json"
	self.__objects = {}

    def all(self):
        """all function"""
        return self.__objects

    	
