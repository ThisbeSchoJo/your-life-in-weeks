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
        if (type(value) == str) and (len(value) > 0):
            self._category = value
        else:
            raise Exception("Error: Category must ne a string that is at least 1 character long!")

    @property   
    def week_id_getter(self):
        return self._week_id
    
    @week_id_getter.setter
    def week_id(self, value):
        if type(value) == int:
            self._week_id = value
        else:
            raise Exception("Error: Week ID must be an integer!")
        
    @classmethod
    def create_table(cls):
        sql='''
            CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY,
            events TEXT,
            category TEXT,
            week_id INTEGER
            )
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql='''
            DROP TABLE IF EXISTS comments
        '''

        CURSOR.execute(sql)

    def __repr__(self):
        return f"<Comment: # {self.id} - Events: {self.events}, Category: {self.category}, Week ID: {self.week_id}>"
