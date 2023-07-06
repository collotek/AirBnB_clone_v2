#!/usr/bin/python3
""" This is file storage class for AirBnB """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a list of object of one type of class"""
        if cls is not None:
            # create a new dictionary of objects to passed cls
            # key must be the same as in __objects
            obj_dict = {key: FileStorage.__objects[key] for key
                        in FileStorage.__objects.keys() if
                        FileStorage.__objects[key].__class__ == cls}
            return obj_dict
        # return all objects if class is not specified
        return FileStorage.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete object inside __objects dictionary"""
        if obj is not None:
            # check if object is in dictionary
            key = ".".join([obj.to_dict()['__class__'], obj.id])
            if key in FileStorage.__objects.keys():
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """ calls reload()
        """
        self.reload()
