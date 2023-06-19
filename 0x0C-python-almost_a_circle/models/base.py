#!/usr/bin/python3
'''base'''

import json
import csv


class Base:
    '''Declares the base model'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        converts a list of dictionaries to a json string
        Args:
            list_dictionaries(list): list of dictionaries to convert
        Return:
            json string
        '''
        if not isinstance(list_dictionaries, list) or \
                len(list_dictionaries) == 0 or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        saves a list of objects to a json file
        Args:
            list_objs(list): list of objects to save
        '''
        filename = str(cls.__name__) + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                dictionary_list = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dictionary_list))

    @staticmethod
    def from_json_string(json_string):
        '''
        converts a json string to a python object
        Args:
            json_string(str): json string to convert
        Return:
            python object
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        creates a new instance of the class using the key-worded
        argument dictionary
        '''
        if dictionary and len(dictionary) > 0:
            if cls.__name__ == 'Rectangle':
                new_instance = cls(5, 4)
            elif cls.__name__ == 'Square':
                new_instance = cls(5)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        '''loads a list of dictionaries from a json file'''
        filename = str(cls.__name__) + '.json'
        try:
            with open(filename, 'r') as f:
                list_of_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**item) for item in list_of_dictionaries]
        except (FileNotFoundError, IOError):
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = str(cls.__name__) + '.csv'
        with open(filename, 'w', newline='') as csv_file:
            if list_objs is None or len(list_objs) == 0:
                csv_file.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fieldnames = ['id', 'size', 'x', 'y']
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = str(cls.__name__) + '.csv'
        try:
            with open(filename, 'r', newline='') as csv_file:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fieldnames = ['id', 'size', 'x', 'y']
                csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                dict_list = []
                for row in csv_reader:
                    new_dict = {}
                    for k, v in row.items():
                        new_dict[k] = int(v)
                    dict_list.append(new_dict)
                return [cls.create(**obj) for obj in dict_list]
        except (FileNotFoundError, IOError):
            return []
