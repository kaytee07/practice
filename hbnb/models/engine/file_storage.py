#!/usr/bin/python3
"""
this class is a filestorage that serializes instances to a JSON fil
and deserializes JSON file to instances
"""
import json
import os
#from models.base_model import BaseModel


class FileStorage:
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """

        """
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, mode = "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode = "r", encoding = "utf-8")\
                 as file:
                data = json.load(file)
                class_to_model = {
                    "BaseModel": "base_model",
                    "User": "user",
                    "State": "state",
                    "City": "city",
                    "Amenity": "amenity",
                    "Place": "place",
                    "Review": "review",
                }
                for key, value in data.items():
                    classname, obj = key.split('.')
                    model = class_to_model[classname]
                    module = __import__(
                        f'models.{model}',  fromlist=[classname])
                    cls = getattr(module, classname)
                    obj_dict = cls(**value)
                    self.__objects[key] = obj_dict
