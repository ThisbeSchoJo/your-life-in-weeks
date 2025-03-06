from models.week import Week
from models.user import User
from models.comment import Comment


def seed_database():
    Week.drop_table()
    User.drop_table()
    Week.create_table()
    User.create_table()

    Week.create(1, "2024-12-17", 8, "Went to Norway and Spain with AG - went dogsledding, saw the northern lights! And had a lot of patatas bravas<3")
    Week.create(1, "2025-01-01", 1, "First week in NYC! Unfortunately I was down bad this week though...")
    Week.create(1, "2025-01-07", 9, "Was exciting to start class and loved the material and meeting everyone! EG came back from his trip this week and Frankie came back from NH!! Think I was fully feeling the W finally.")
    Week.create(1, "2025-01-14", 8, "Things were still good! Enjoying NYC and being social and classes were going very well.")
    Week.create(1, "2025-02-04", 7, "Was EG's birthday week so there were a lot of festivities. AG came up for it and that was ~a lot~ but overall very very good to see her. Also met Meena! Whom I now love and hope to see again.")
    Week.create(1, "2025-02-11", 9, "Flew to FL for the weekend to celebrate SC's birthday and got to meet all her friends (loved them all). Went to the beach and enjoyed the good weather and just went for some nice walks and got some plant cuttings to gift to Alanah!")
    Week.create(1, "2025-02-18", 6, "Was a short week at school and Python stuff was fun. Did a lot of ruminating this week though.")
    Week.create(1, "2025-02-25", 1, "Missed AG a lot this week and got a bit stressed with school. LH got mad at me for things with SC.")
    Week.create(1, "2025-03-04", 9, "Me and AG had a good talk and me and LH made up. SC came to visit me and we went to Bathhouse. Finished Phase 3 at Flatiron Bootcamp. Python was fun :). EG is on a work trip so I'm home aloneee!")

    User.create("Thisbe", "1995-10-04")
    User.create("Sydney", "1998-02-14")
    User.create("Tosca", "1993-09-20")
    User.create("Tatiana", "1990-12-06")

    print("Weeks successfully seeded!")
    print("Week.all after seeding:", Week.all)

seed_database()