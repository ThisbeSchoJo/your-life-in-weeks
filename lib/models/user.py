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
        
    def weeks_lived(self):
        today = datetime.today().date()
        days_lived = (today - self._birthdate).days #gets the number of days lived
        weeks_lived = (days_lived//7) #converts the days lived to weeks
        return weeks_lived
    
    def weeks_left(self):
        total_weeks = 90 * 52 #90 years * 52 weeks per year
        weeks_lived = self.weeks_lived()
        weeks_left = total_weeks - weeks_lived
        return weeks_left
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                birthdate TEXT
            )
        '''
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS users
        '''
        CURSOR.execute(sql)
    
    def save(self):
        sql = '''
            INSERT INTO users (name, birthdate)
            VALUES (?, ?)
        '''
        CURSOR.execute(sql, (self.name, self.birthdate.strftime("%Y-%m-%d")))
        CONN.commit()
        self.id = CURSOR.lastrowid
        User.all.append(self)
    
    @classmethod
    def create(cls, name, birthdate):
        new_user = cls(name, birthdate)
        new_user.save()
        return new_user
    
    @classmethod
    def instance_from_db(cls, row):
        new_user = cls(row[1], row[2], row[0])
        return new_user
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM users
        '''
        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM users
            WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    
    def delete(self):
        sql = '''
            DELETE FROM users
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        User.all = [user for user in User.all if user.id !=self.id]

    def __repr__(self):
        return f"<User #{self.id} - Name: {self.name}, Birthdate: {self.birthdate}>"