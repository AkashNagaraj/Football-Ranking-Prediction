import sqlite3
conn=sqlite3.connect("/home/linuxbox/Desktop/Stats-Football/database.sqlite")
c=conn.cursor()
print(c)