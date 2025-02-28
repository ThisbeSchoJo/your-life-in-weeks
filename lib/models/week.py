from models.__init__ import CONN, CURSOR

class Week:
    
    def __init__(self, user, date, satisfaction_rating, comments):
        self.user = user
        self.date = date
        self.satisfaction_rating = satisfaction_rating
        self.comments = comments

    @property
    def user_getter():
        pass