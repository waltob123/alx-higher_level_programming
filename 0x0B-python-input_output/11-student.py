#!/usr/bin/python3
'''11-student.py module'''


class Student:
    '''Defines a Student class'''

    def __init__(self, first_name, last_name, age):
        '''
        Initializes a Student class with first_name, last_name
        and age.

        Args:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.
        If attrs is a list of strings, only attributes name
        contain in this list must be retrieved. Otherwise, all
        attributes must be retrieved

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
