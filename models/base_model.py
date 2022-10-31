#!/usr/bin/python3
"""
BaseModel module
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Defines common attributes/methods for other classes"""
    
    def __init__(self, *args, **kwargs):
        """initializes BaseModel attributes"""
        
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        ft = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for key, n in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(n, ft)
                else:
                    self.__dict__[key] = n
        models.storage.new(self)
    def save(self):
        """updated_at attribute with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()
        
    def to_dict(self):
        """returns BaseModel dictonary"""
        Bdic = self.__dict__.copy()
        Bdic["created_at"] = self.created_at.isoformat()
        Bdic["updated_at"] = self.updated_at.isoformat()
        Bdic["__class__"] = self.__class__.__name__
        return Bdic
    def __str__(self):
        """returns a string representation of instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    
