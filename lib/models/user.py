from datetime import datetime
from models.__init__ import CONN, CURSOR

class User:

    all = []

    def __init__(self, name, birthdate, id=None):
        self.name = name
        self.birthdate = birthdate
        self.id = id

    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, name_value):
        if (type(name_value) == str) and len(name_value) > 0:
            self._name = name_value
        else:
            raise ValueError("Name must be a string at least 1 character long!")
        
    @property
    def birthdate_getter(self):
        return self.birthdate
    
    @birthdate_getter.setter
    def birthdate(self, value):
        if (type(value) == str) and (len(value) == 10):
            self._birthdate = datetime.strptime(value, "%Y-%m-%d").date()
        else:
            raise ValueError("Birthdate must be a string in YYYY-MM-DD format!")
        