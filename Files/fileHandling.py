# names = str(input("What is the name?"))
# f = open("word.txt", "a")
# f.write(f"{names}\n")
# f.close()

import sqlite3
con = sqlite3.connect("students.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM Students")


for i in res.fetchall():
    f = open("allData.txt", "a")
    f.write(f"{i}\n")
    f.close()

    

