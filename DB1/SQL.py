import sqlite3
con = sqlite3.connect("New.db")

cur = con.cursor()

# cur.execute("""
#             INSERT INTO movie VALUES 
#             ('Monty Python', 1975,8.2),
#             ('Wednesday',2023,8.5)
#             """)

# con.commit()

#Fetching data from database
# res= cur.execute("SELECT score FROM movie")
# print(res.fetchall())


# cur.execute("""
#             INSERT INTO movies VALUES 
#             ("2","Power", "2023","8.6"),
#             ("3","Mission Impossible","2023","8.0")
#             """)

# con.commit()

allresults = cur.execute("SELECT * FROM movie")
for i in allresults:
    f=open("book.txt", "a")
    f.write(f"{i}\n")
    f.close()




