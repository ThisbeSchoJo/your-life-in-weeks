from models.week import Week
from models.user import User
from models.comment import Comment


def seed_database():
    Week.drop_table()
    User.drop_table()
    Week.create_table()
    User.create_table()

    Week.create(1, "2025-01-01", 1, "bad time")
    Week.create(1, "2025-01-10", 9, "started classes!")
    Week.create(1, "2025-03-01", 8, "Enjoying all the change!")

    User.create("Thisbe", "1995-10-04")
    User.create("Sydney", "1998-02-14")

    print("Weeks successfully seeded!")

seed_database()