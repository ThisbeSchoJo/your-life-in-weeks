from datetime import datetime
from models.__init__ import CONN, CURSOR
from models.user import User

class Week:

    all = []
    
    def __init__(self, user_id, date, satisfaction_rating, comments):
        # self.user = user
        self.user_id = user_id
        self.date = date
        self.satisfaction_rating = satisfaction_rating
        self.comments = comments
        self.id = None

    @property
    def user_id_getter(self):
        return self._user_id
    
    @user_id_getter.setter
    def user_id(self, value):
        if (isinstance(value, int)):
            self._user_id = value
        else:
            raise Exception("Error: User must be an integer!")
        
    @property
    def date_getter(self):
        return self._date
    
    @date_getter.setter
    def date(self, value):
        if (type(value) == str) and (len(value) == 10):
            self._date = datetime.strptime(value, "%Y-%m-%d").date()
        else:
            raise Exception("Date must be a string and in YYYY-MM-DD format!")
        
    @property
    def satisfaction_rating_getter(self):
        return self._satisfaction_rating
    
    @satisfaction_rating_getter.setter
    def satisfaction_rating(self, value):
        if (type(value) == int) and (0 < value < 10):
            self._satisfaction_rating = value
        else:
            raise Exception("Error: Satisfaction rating must be an integer between 1 and 10!")
        
    @property
    def comments_getter(self):
        return self._comments
    
    @comments_getter.setter
    def comments(self, value):
        if (type(value) == str) and (len(value) > 0):
            self._comments = value
        else:
            raise Exception("Comments must be a string at least 1 character long!")

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS weeks (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                date TEXT,
                satisfaction_rating INTEGER,
                comments TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS weeks
        '''

        CURSOR.execute(sql)

    @classmethod
    def create(cls, user_id, date, satisfaction_rating, comments):
        new_week = cls(user_id, date, satisfaction_rating, comments)
        new_week.save()
        return new_week
    
    @classmethod
    def instance_from_db(cls, row):
        user_id = row[1] #Get user_id from the database row
        user = User.find_by_id(user_id) #Fetch the actual User instance
        if user is None:
            raise Exception(f"Error: No User found with ID {user_id}")
        week = cls(user.id, row[2], row[3], row[4])
        week.id = row[0]
        return week

    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM weeks
        '''

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]

        return cls.all

    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM weeks
            WHERE id = ?
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        return None
    
    def calculate_week_number(self):
        # Fetch user's birthdate
        user = User.find_by_id(self.user_id)
        if user is None:
            raise Exception(f"User with ID {self.user_id} not found!")
        
        # Get number of weeks the user has lived
        weeks_lived = user.weeks_lived()

        # Calculate the difference in weeks between the user's birthdate and the logged week date
        days_since_birth = (self.date - user.birthdate).days
        weeks_since_birth = days_since_birth // 7
        return weeks_since_birth

    def save(self):
        sql = '''
            INSERT INTO weeks (user_id, date, satisfaction_rating, comments) 
            VALUES (?, ?, ?, ?)
        '''

        CURSOR.execute(sql, (self.user_id, self.date.strftime("%Y-%m-%d"), self.satisfaction_rating, self.comments))
        CONN.commit()
        self.id = CURSOR.lastrowid

        Week.all.append(self)

    def delete(self):
        sql = '''
            DELETE FROM weeks
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Week.all = [week for week in Week.all if week.id != self.id]

    def comment(self):
        from models.comment import Comment

        sql = '''
            SELECT * FROM comments
            WHERE week_id = ?
        '''

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Comment.instance_from_db(row) for row in rows]

    def filter_weeks_by_satisfaction(self, min_rating=5):
        Week.get_all()
        for week in Week.all:
            if week.satisfaction_rating >= min_rating:
                user = User.find_by_id(week.user_id)
                print(f"Week ID: {week.id}, User: {user.name}, Date: {week.date}, Saisfaction Rating: {week.satisfaction_rating}/10")
                print(f"Week summary: {week.comments}")
                print("-" *40) #Adds a separator line
    
    def __repr__(self):
        user = User.find_by_id(self.user_id)
        return f"<Week {self.id} - User: {user.name if user else 'Unknown'}, Date: {self.date}, Satisfaction Rating: {self.satisfaction_rating}, Comments: {self.comments}>"
    