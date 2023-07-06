#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a list of object of one type of class"""
        if cls is not None:
            # create a new dictionary of objects fo passed cls
            # key must be the same as in __objects
            obj_dict = {key: FileStorage.__objects[key] for key
                        in FileStorage.__objects.keys() if
                        FileStorage.__objects[key].__class__ == cls}
            return obj_dict
        # return all objects if class is not specified
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update(
            {'{}.{}'.format(obj.to_dict()['__class__'], obj.id): obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    FileStorage.__objects[key] = classes[
                        val['__class__']](**val)
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
        """Temporary documentation"""
        self.reload()
