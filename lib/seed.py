from models.week import Week
from models.comment import Comment


def seed_database():
    Week.drop_table()
    Week.create_table()

    Week.create("Thisbe", 12025, 1, "bad time")
    Week.create("Thisbe", 22025, 9, "started classes!")
    Week.create("Thisbe", 32025, 8, "Enjoying all the change!")

    print("Weeks successfully seeded!")

seed_database