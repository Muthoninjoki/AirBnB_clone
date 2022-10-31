#!/usr/bin/python3
"""file storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes and deserializes instances to a json file"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the object dictionary"""
        return FileStorage.__objects
      
    def new(self, obj):
        """sets in object with key obj class name id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj
