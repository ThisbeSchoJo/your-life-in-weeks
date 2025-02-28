from models.__init__ import CONN, CURSOR

class Week:
    
    def __init__(self, user, date, satisfaction_rating, comments):
        self.user = user
        self.date = date
        self.satisfaction_rating = satisfaction_rating
        self.comments = comments

    @property
    def user_getter(self):
        return self._user
    
    @user_getter.setter
    def user(self, value):
        if (type(value) == str) and (len(value) > 4):
            self._user = value
        else:
            raise Exception("Error: User must be a string that is at least 5 characters long!")
        
    @property
    def date_getter(self):
        return self._date
    
    @date_getter.setter
    def date(self, value):
        # MIGHT NEED TO CHANGE VALUE DATA TYPE
        if (type(value) == int) and (value > 0):
            self._date = value
        else:
            raise Exception("Date must be an integer and at least 1 character long!")
        
    @property
    def satisfaction_rating_getter(self):
        return self._satisfaction_rating
    
    @satisfaction_rating_getter.setter
    def satisfaction_rating(self, value):
        if (type(value) == int) and (len(value) > 0):
            self._satisfaction_rating = value
        else:
            raise Exception("Error: Satisfaction rating must be an integer that is at least 1 character long!")