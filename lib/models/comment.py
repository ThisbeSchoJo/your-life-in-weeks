from models.__init__ import CONN, CURSOR

class Comment:
    
    def __init__(self, events, week_id, category):
        self.events = events
        self.week_id = week_id
        self.category = category
        self.id = None

    @property
    def category_getter(self):
        return self._category
    
    @category_getter.setter
    def category(self, value):
        # WILL PROBABLY NEED TO CHANGE THIS VALIDATION
        if (type(value) == int) and (value > 0):
            self._category = value
        else:
            raise Exception("Error: Category must ne an integer that is greater than 0!")

    @property   
    def week_id_getter(self):
        return self._week_id
    
    @week_id_getter.setter
    def week_id(self, value):
        if type(value) == int:
            self._week_id = value
        else:
            raise Exception("Error: Week ID must be an integer!")
        
    

    def __repr__(self):
        return f"<Comment: # {self.id} - Events: {self.events}, Category: {self.category}, Week ID: {self.week_id}>"
