from models.__init__ import CONN, CURSOR

class Comment:

    all = []
    
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
            week_id INTEGER,
            FOREIGN KEY(week_id) REFERENCES weeks(id)
            )
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql='''
            DROP TABLE IF EXISTS comments
        '''

        CURSOR.execute(sql)

    def save(self):
        sql = '''
            INSERT INTO comments (events, category, week_id) 
            VALUES (?, ?, ?)
        '''

        CURSOR.execute(sql, (self.events, self.category, self.week_id))

        self.id = CURSOR.lastrowid

        Comment.all.append(self)
    
    @classmethod
    def create(cls, events, week_id, category):
        new_comment = cls(events, week_id, category)
        new_comment.save()
        return new_comment
    
    @classmethod
    def instance_from_db(cls, row):
        new_comment = cls(row[1], row[2])
        new_comment.id = row[0]
        return new_comment

    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM comments
        '''

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM comments
            WHERE id = ?
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def delete(self):
        sql = '''
            DELETE FROM comments
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Comment.all = [comment for comment in Comment.all if comment.id != self.id]

    def __repr__(self):
        return f"<Comment: # {self.id} - Events: {self.events}, Category: {self.category}, Week ID: {self.week_id}>"
