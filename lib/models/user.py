from models.__init__ import CONN, CURSOR

class User:
    all = []

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.id = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_value):
        if (type(name_value) == str) and len(name_value) > 0:
            self._name = name_value
        else:
            raise ValueError("Name must be a string at least 1 character long!")