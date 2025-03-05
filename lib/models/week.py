from datetime import datetime
from models.__init__ import CONN, CURSOR
from models.user import User

class Week:

    all = []
    
    def __init__(self, user, date, satisfaction_rating, comments):
        self.user = user
        self.user_id = user.id
        self.date = date
        self.satisfaction_rating = satisfaction_rating
        self.comments = comments
        self.id = None

    @property
    def user_getter(self):
        return self._user
    
    @user_getter.setter
    def user(self, value):
        if (isinstance(value, User)):
            self._user = value
            self.user_id = value.id
        else:
            raise Exception("Error: User must be an instance of the User class!")
        
    @property
    def date_getter(self):
        return self._date
    
    @date_getter.setter
    def date(self, value):
        # MIGHT NEED TO CHANGE VALUE DATA TYPE
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
        
    # NEED TO ADD THE OTHER PROPERTIES

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

    def save(self):
        sql = '''
            INSERT INTO weeks (user_id, date, satisfaction_rating, comments) 
            VALUES (?, ?, ?, ?)
        '''

        CURSOR.execute(sql, (self.user_id, self.date.strftime("%Y-%m-%d"), self.satisfaction_rating, self.comments))
        CONN.commit()
        self.id = CURSOR.lastrowid

        Week.all.append(self)

    @classmethod
    def create(cls, user, date, satisfaction_rating, comments):
        new_week = cls(user, date, satisfaction_rating, comments)
        new_week.save()
        return new_week
    
    @classmethod
    def instance_from_db(cls, row):
        user = User.find_by_id(row[1])
        new_week = cls(user, row[2], row[3], row[4])
        new_week.id = row[0]
        return new_week

    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM weeks
        '''

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]

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


    def __repr__(self):
        return f"<Week {self.id} - User: {self.user}, Date: {self.date}, Satisfaction Rating: {self.satisfaction_rating}, Comments: {self.comments}>"
    