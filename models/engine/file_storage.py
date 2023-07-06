#!/usr/bin/python3
""" This is file storage class for AirBnB """
import json


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
        FileStorage.__objects.update(
            {'{}.{}'.format(obj.to_dict()['__class__'], obj.id): obj})

    def save(self):
        """serialize the file path to JSON file path
        """
        with open(FileStorage.__file_path, 'w') as f:
            my_dict = {}
            my_dict.update(FileStorage.__objects)
            for key, val in my_dict.items():
                my_dict[key] = val.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
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
            tempo = {}
            with open(FileStorage.__file_path, 'r') as f:
                tempo = json.load(f)
                for key, value in tempo.items():
                    FileStorage.__objects[key] = classes[
                        value['__class__']](**value)
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
