#!/usr/bin/python3
""" module point 1 base class """


class BaseModel:
    """class BaseModel"""

    def __init__(self, my_number=0, name=""):
        """init function"""
        self.id = str(uuid.uuid4())
	self.my_number = my_number
	self.name = name       
        self.created_at = datetime()
	self.updated_at = save()

    def __str__(self):
        """str function"""
        return "[{}] ({}) {}".format(self.__name__, self.id, self.__dict__)

    def save(self):
        """save function"""
        self.updated_at = datetime()

    def to_dict(self):
        """to_dict function"""
        return {'my_number': self.my_number, 'name': self.name, '__class__\
': 		
